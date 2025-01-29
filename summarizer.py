import requests
from bs4 import BeautifulSoup
import openai
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_website(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        # Remove unwanted tags
        for tag in soup(["script", "style", "img", "input"]):
            tag.decompose()

        text = soup.get_text(separator="\n", strip=True)

        # Send text to OpenAI for summarization
        response = openai.chat.completions.create(
            model="gpt-4o-mini",  # Keep the model same as in the .ipynb file
            messages=[
                {"role": "system", "content": "Summarize the following text. If there are any news and announcements, include them as well, please give me the response in bullet points with proper side headings"},  # Keep system prompt
                {"role": "user", "content": text}  # Keep user prompt
            ]
        )

        return response.choices[0].message.content
    
    except Exception as e:
        return f"Error: {e}"
