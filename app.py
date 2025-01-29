import streamlit as st
from summarizer import summarize_website

st.set_page_config(page_title="Website Summarizer", layout="wide")

# Top Heading with Styling
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🌍 Website Summarizer</h1>", unsafe_allow_html=True)

st.write("Enter a URL and get a concise summary!")

# URL Input
url = st.text_input("🔗 Enter Website URL:")

# Summarize Button
if st.button("Summarize"):
    if url:
        summary = summarize_website(url)
        st.subheader("📌 Summary")
        st.write(summary)
    else:
        st.warning("⚠️ Please enter a valid URL.")
