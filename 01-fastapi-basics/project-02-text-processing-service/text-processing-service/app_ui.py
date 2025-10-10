import streamlit as st
import requests
import json
from collections import Counter
import plotly.express as px
import plotly.graph_objects as go

# API Configuration
API_URL = "http://localhost:8000"

# Page Config
st.set_page_config(
    page_title="Text Processing Tool",
    page_icon="📝",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">📝 Text Processing Tool</h1>', unsafe_allow_html=True)
st.markdown("---")

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    operation = st.selectbox(
        "Choose Operation",
        ["Text Cleaning", "Tokenization", "Text Statistics", "Word Frequency", "N-grams", "Sentiment Analysis"]
    )
    st.markdown("---")
    st.info("💡 Enter your text and select an operation to analyze it.")

# Main Content
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📥 Input Text")
    input_text = st.text_area(
        "Enter your text here:",
        height=300,
        placeholder="Type or paste your text here...",
        help="Enter the text you want to process"
    )

with col2:
    st.subheader("📤 Results")
    result_container = st.container()

# Process button
if st.button("🚀 Process Text", type="primary", use_container_width=True):
    if not input_text.strip():
        st.error("⚠️ Please enter some text to process!")
    else:
        with st.spinner("Processing..."):
            try:
                # Text Cleaning
                if operation == "Text Cleaning":
                    with st.expander("🔧 Cleaning Options", expanded=True):
                        c1, c2, c3 = st.columns(3)
                        with c1:
                            lowercase = st.checkbox("Lowercase", value=True)
                            remove_punct = st.checkbox("Remove Punctuation", value=True)
                        with c2:
                            remove_nums = st.checkbox("Remove Numbers", value=False)
                            remove_space = st.checkbox("Remove Extra Spaces", value=True)
                        with c3:
                            normalize = st.checkbox("Normalize Unicode", value=True)
                    
                    response = requests.post(f"{API_URL}/clean", json={
                        "text": input_text,
                        "lowercase": lowercase,
                        "remove_punctuation": remove_punct,
                        "remove_numbers": remove_nums,
                        "remove_extra_whitespace": remove_space,
                        "normalize_unicode": normalize
                    })
                    
                    if response.status_code == 200:
                        result = response.json()
                        with result_container:
                            st.success("✅ Text cleaned successfully!")
                            st.text_area("Cleaned Text:", result["cleaned_text"], height=300)
                
                # Tokenization
                elif operation == "Tokenization":
                    method = st.radio("Tokenization Method:", ["word", "sentence", "char"], horizontal=True)
                    lowercase_tok = st.checkbox("Lowercase tokens", value=False)
                    
                    response = requests.post(f"{API_URL}/tokenize", json={
                        "text": input_text,
                        "method": method,
                        "lowercase": lowercase_tok
                    })
                    
                    if response.status_code == 200:
                        result = response.json()
                        with result_container:
                            st.success(f"✅ Found {result['count']} tokens!")
                            st.metric("Token Count", result['count'])
                            st.write("**Tokens:**")
                            st.json(result['tokens'][:50])  # Show first 50
                            if len(result['tokens']) > 50:
                                st.info(f"Showing first 50 of {len(result['tokens'])} tokens")
                
                # Text Statistics
                elif operation == "Text Statistics":
                    response = requests.post(f"{API_URL}/stats", json={"text": input_text})
                    
                    if response.status_code == 200:
                        stats = response.json()
                        with result_container:
                            st.success("✅ Statistics calculated!")
                            
                            # Metrics in columns
                            m1, m2, m3 = st.columns(3)
                            m1.metric("📊 Characters", stats['character_count'])
                            m2.metric("📝 Words", stats['word_count'])
                            m3.metric("📄 Sentences", stats['sentence_count'])
                            
                            m4, m5, m6 = st.columns(3)
                            m4.metric("🔤 Avg Word Length", f"{stats['average_word_length']:.2f}")
                            m5.metric("✨ Unique Words", stats['unique_words'])
                            m6.metric("📏 No Spaces", stats['character_count_no_spaces'])
                            
                            # Bar chart
                            fig = go.Figure(data=[
                                go.Bar(
                                    x=['Characters', 'Words', 'Sentences', 'Unique Words'],
                                    y=[stats['character_count'], stats['word_count'], 
                                       stats['sentence_count'], stats['unique_words']],
                                    marker_color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
                                )
                            ])
                            fig.update_layout(title="Text Statistics Overview", height=400)
                            st.plotly_chart(fig, use_container_width=True)
                
                # Word Frequency
                elif operation == "Word Frequency":
                    top_n = st.slider("Show top N words:", 5, 50, 15)
                    
                    response = requests.post(f"{API_URL}/word-frequency", json={"text": input_text})
                    
                    if response.status_code == 200:
                        result = response.json()
                        with result_container:
                            st.success(f"✅ Found {result['unique_words']} unique words!")
                            
                            # Get top N words
                            top_words = result['word_frequencies'][:top_n]
                            words = [item['word'] for item in top_words]
                            freqs = [item['frequency'] for item in top_words]
                            
                            # Bar chart
                            fig = px.bar(
                                x=freqs, 
                                y=words, 
                                orientation='h',
                                labels={'x': 'Frequency', 'y': 'Word'},
                                title=f'Top {top_n} Most Common Words'
                            )
                            fig.update_layout(height=500)
                            st.plotly_chart(fig, use_container_width=True)
                            
                            # Word cloud style display
                            st.write("**All Word Frequencies:**")
                            st.dataframe(result['word_frequencies'], height=300)
                
                # N-grams
                elif operation == "N-grams":
                    n = st.slider("N-gram size:", 2, 5, 2)
                    top_k = st.slider("Show top N n-grams:", 5, 30, 10)
                    
                    response = requests.post(f"{API_URL}/ngrams", json={
                        "text": input_text,
                        "n": n,
                        "top_k": top_k
                    })
                    
                    if response.status_code == 200:
                        result = response.json()
                        with result_container:
                            st.success(f"✅ Found {result['unique_ngrams']} unique {n}-grams!")
                            
                            col_a, col_b = st.columns(2)
                            col_a.metric("Total N-grams", result['total_ngrams'])
                            col_b.metric("Unique N-grams", result['unique_ngrams'])
                            
                            # Chart
                            ngrams_list = result['ngrams'][:top_k]
                            ngram_names = [item['ngram'] for item in ngrams_list]
                            ngram_freqs = [item['frequency'] for item in ngrams_list]
                            
                            fig = px.bar(
                                x=ngram_freqs,
                                y=ngram_names,
                                orientation='h',
                                labels={'x': 'Frequency', 'y': f'{n}-gram'},
                                title=f'Top {top_k} Most Common {n}-grams'
                            )
                            fig.update_layout(height=500)
                            st.plotly_chart(fig, use_container_width=True)
                
                # Sentiment Analysis
                elif operation == "Sentiment Analysis":
                    response = requests.post(f"{API_URL}/sentiment", json={"text": input_text})
                    
                    if response.status_code == 200:
                        result = response.json()
                        with result_container:
                            sentiment = result['sentiment']
                            score = result['score']
                            
                            # Sentiment emoji
                            emoji_map = {
                                "positive": "😊",
                                "negative": "😞",
                                "neutral": "😐"
                            }
                            
                            st.success("✅ Sentiment analyzed!")
                            
                            # Big sentiment display
                            col_s1, col_s2, col_s3 = st.columns([1, 2, 1])
                            with col_s2:
                                st.markdown(f"<h1 style='text-align: center;'>{emoji_map[sentiment]}</h1>", 
                                          unsafe_allow_html=True)
                                st.markdown(f"<h2 style='text-align: center;'>{sentiment.upper()}</h2>", 
                                          unsafe_allow_html=True)
                            
                            # Metrics
                            m1, m2, m3 = st.columns(3)
                            m1.metric("😊 Positive Words", result['positive_words'])
                            m2.metric("😞 Negative Words", result['negative_words'])
                            m3.metric("📊 Score", f"{score:.3f}")
                            
                            # Gauge chart
                            fig = go.Figure(go.Indicator(
                                mode="gauge+number",
                                value=score,
                                domain={'x': [0, 1], 'y': [0, 1]},
                                title={'text': "Sentiment Score"},
                                gauge={
                                    'axis': {'range': [-1, 1]},
                                    'bar': {'color': "darkblue"},
                                    'steps': [
                                        {'range': [-1, -0.3], 'color': "lightcoral"},
                                        {'range': [-0.3, 0.3], 'color': "lightgray"},
                                        {'range': [0.3, 1], 'color': "lightgreen"}
                                    ],
                                }
                            ))
                            st.plotly_chart(fig, use_container_width=True)
                
            except requests.exceptions.ConnectionError:
                st.error("❌ Cannot connect to API. Make sure the FastAPI server is running on http://localhost:8000")
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>Made with ❤️ using Streamlit & FastAPI</div>",
    unsafe_allow_html=True
)