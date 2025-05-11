import streamlit as st
import fitz  
import requests
import os
import csv
from datetime import datetime

OPENROUTER_API_KEY = "sk-or-v1-********************************************"
OPENROUTER_BASE_URL = "https://openai/api/v1/chat/completions"
LOG_FILE = "chat_history.csv"

def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def ask_question(text, question, model="openai/gpt-3.5-turbo"):
    prompt = f"You are a helpful assistant. The document says:\n{text}\n\nUser's question: {question}"

    headers = {
        "Authorization": f"Bearer {OPENRAPI_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(OPENROUTER_BASE_URL, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"❌ Error: {response.status_code} - {response.text}"

def log_interaction(pdf_name, question, answer):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_exists = os.path.isfile(LOG_FILE)
    with open(LOG_FILE, mode="a", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Timestamp", "PDF Name", "User Question", "AI Answer"])
        writer.writerow([timestamp, pdf_name, question, answer])

st.set_page_config(page_title="Chat with your PDF")
st.title("📄 ChatPDF using OpenRouter")
st.write("Upload a PDF file and ask questions about its content.")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    with st.spinner("Reading PDF..."):
        pdf_text = extract_text_from_pdf(uploaded_file)
        st.success("✅ PDF processed successfully!")

    user_question = st.text_input("Ask a question about the PDF:")

    if user_question:
        with st.spinner("Generating answer..."):
            answer = ask_question(pdf_text, user_question)
            st.markdown("### 🧠 Answer:")
            st.write(answer)

            log_interaction(uploaded_file.name, user_question, answer)
            st.success("📝 Interaction saved to history.")
