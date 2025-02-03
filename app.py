import streamlit as st
from summarizer import summarize_website

# Page configuration
st.set_page_config(
    page_title="Website Summarizer",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Dark theme styling
st.markdown("""
<style>
    /* Global styles */
    .stApp {
        background-color: #0F172A;
    }
    .main {
        padding: 2rem;
    }
    
    /* Container styling */
    .content-container {
        max-width: 800px;
        margin: 2rem auto;
        padding: 2.5rem;
        background-color: #1E293B;
        border-radius: 16px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
    }
    
    /* Header styling */
    .header {
        text-align: center;
        margin-bottom: 3.5rem;
    }
    .title {
        background: linear-gradient(120deg, #60A5FA, #818CF8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.75rem;
        font-weight: 700;
        margin-bottom: 1rem;
        letter-spacing: -0.02em;
    }
    .subtitle {
        color: #94A3B8;
        font-size: 1.15rem;
        line-height: 1.6;
    }
    
    /* Input field styling */
    .stTextInput > div > div > input {
        background-color: #334155;
        border: 2px solid #475569;
        border-radius: 12px;
        padding: 0.875rem 1.25rem;
        font-size: 1rem;
        transition: all 0.2s ease;
        color: #E2E8F0;
    }
    .stTextInput > div > div > input:focus {
        background-color: #334155;
        border-color: #60A5FA;
        box-shadow: 0 0 0 4px rgba(96, 165, 250, 0.1);
    }
    .stTextInput > div > div > input::placeholder {
        color: #94A3B8;
    }
    
    /* Button styling */
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #60A5FA, #818CF8);
        color: white;
        padding: 0.875rem 1.5rem;
        border-radius: 12px;
        border: none;
        font-weight: 600;
        font-size: 1.05rem;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #3B82F6, #6366F1);
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(96, 165, 250, 0.2);
    }
    
    /* Summary container styling */
    .summary-box {
        margin-top: 2.5rem;
        padding: 2rem;
        background-color: #334155;
        border: 2px solid #475569;
        border-radius: 12px;
        transition: all 0.3s ease;
    }
    .summary-box:hover {
        border-color: #60A5FA;
        box-shadow: 0 4px 12px rgba(96, 165, 250, 0.1);
    }
    .summary-header {
        color: #60A5FA;
        font-size: 1.35rem;
        font-weight: 600;
        margin-bottom: 1.25rem;
    }
    .summary-text {
        color: #E2E8F0;
        line-height: 1.75;
        font-size: 1.05rem;
    }
    
    /* Warning message styling */
    .stAlert {
        background-color: #991B1B;
        border: 2px solid #B91C1C;
        border-radius: 12px;
        padding: 1.25rem;
        color: #FEE2E2;
    }
    
    /* Spinner styling */
    .stSpinner > div {
        border-color: #60A5FA !important;
    }
    
    /* Footer styling */
    .footer {
        text-align: center;
        padding-top: 3rem;
        color: #94A3B8;
        font-size: 0.925rem;
        font-weight: 500;
    }

    /* Help text styling */
    .stTextInput > div > div > small {
        color: #94A3B8 !important;
    }
</style>
""", unsafe_allow_html=True)

# Main container
st.markdown("""
<div class="content-container">
    <div class="header">
        <h1 class="title">Website Summarizer</h1>
        <p class="subtitle">Transform any web content into clear, concise summaries instantly</p>
    </div>
""", unsafe_allow_html=True)

# URL Input
url = st.text_input(
    "",
    placeholder="Enter website URL (e.g., https://example.com)",
    help="Please include the complete URL starting with https://"
)

# Process button
if st.button("Generate Summary"):
    if url:
        try:
            with st.spinner('Analyzing content...'):
                summary = summarize_website(url)
                st.markdown("""
                <div class="summary-box">
                    <div class="summary-header">Summary</div>
                    <div class="summary-text">{}</div>
                </div>
                """.format(summary), unsafe_allow_html=True)
        except Exception as e:
            st.error("Unable to process the URL. Please check if the URL is valid and try again.")
    else:
        st.warning("Please enter a URL to generate a summary")

# Footer
st.markdown("""
    
</div>
""", unsafe_allow_html=True)