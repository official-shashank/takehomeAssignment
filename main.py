import streamlit as st
from openai import OpenAI
import os

# Set your OpenAI API key here directly
api_key = "Enter your open ai key here"
client = OpenAI(api_key=api_key)

# Streamlit page configuration
st.set_page_config(page_title="AI-Enhanced Content Generation", layout="wide")

st.title("AI-Enhanced Content Generation Application")

# Sidebar menu
menu = ["Text Generation", "Text Summarization", "Language Translation"]
choice = st.sidebar.selectbox("Choose a Feature", menu)

def generate_text(prompt, max_tokens):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_tokens
    )
    return completion.choices[0].message['content'].strip()

def summarize_text(text):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Please summarize the following text: {text}"}
        ],
        max_tokens=150
    )
    return completion.choices[0].message['content'].strip()

def translate_text(text, target_language):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Translate the following text to {target_language}: {text}"}
        ],
        max_tokens=150
    )
    return completion.choices[0].message['content'].strip()

if choice == "Text Generation":
    st.subheader("Text Generation")
    
    prompt = st.text_area("Enter a prompt", "")
    max_tokens = st.slider("Max Tokens", 50, 500, 150)
    
    if st.button("Generate Text"):
        if prompt:
            generated_text = generate_text(prompt, max_tokens)
            st.write(generated_text)
        else:
            st.error("Please enter a prompt.")

elif choice == "Text Summarization":
    st.subheader("Text Summarization")
    
    text = st.text_area("Enter text to summarize", "")
    if st.button("Summarize Text"):
        if text:
            summary = summarize_text(text)
            st.write(summary)
        else:
            st.error("Please enter text to summarize.")

elif choice == "Language Translation":
    st.subheader("Language Translation")
    
    text = st.text_area("Enter text to translate", "")
    target_language = st.selectbox("Select target language", ["French", "Spanish", "German", "Chinese"])
    
    if st.button("Translate Text"):
        if text:
            translation = translate_text(text, target_language)
            st.write(translation)
        else:
            st.error("Please enter text to translate.")
