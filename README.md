# 📘 ChatWithPDF – Ask Questions to Your PDFs Using AI

**ChatWithPDF** is a powerful Streamlit-based web app that allows users to upload a PDF and ask natural language questions about its contents. The app uses AI (via OpenRouter) to extract, understand, and answer based on PDF content—making document reading faster and smarter.

🔗 **GitHub Repo:** [Chat-With-PDF](https://github.com/Dattajagan/Chat-With-PDF)

---

## ✨ Features

- 📄 Upload any PDF document
- 💬 Ask natural language questions about the file
- 🧠 AI-powered responses using OpenRouter API
- 📝 Automatic logging of:
  - Uploaded PDF filename
  - User questions
  - AI-generated answers

---

## 💡 Use Cases

- Students analyzing textbooks or notes  
- Researchers summarizing academic papers  
- Professionals reviewing lengthy reports or agreements  
- Anyone who wants quick insights from a document

---

## ⚙️ Tech Stack

- **Frontend:** Streamlit  
- **Backend:** Python  
- **AI Integration:** OpenRouter (ChatGPT-compatible)  
- **PDF Processing:** PyMuPDF (fitz)  
- **Data Logging:** In-memory / CSV

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Dattajagan/Chat-With-PDF.git
cd Chat-With-PDF
2. Install Dependencies

pip install -r requirements.txt
3. Set Up API Key
Create a .env file in the root directory with the following:

OPENROUTER_API_KEY=your_openrouter_api_key
4. Run the Application
streamlit run app.py
🗂️ Project Structure

Chat-With-PDF/
├── app.py              # Main Streamlit app logic
├── .env                # API Key (excluded from Git)
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
└── .gitignore          # Git ignore rules
🔮 Future Improvements
Export Q&A logs to a database or CSV file

Support for multiple PDFs

Summarization and keyword extraction

Dark mode UI and enhanced UX

🧑‍💻 Author
Built with ❤️ by Dattajagan

📜 License
This project is licensed under the MIT License.

yaml

---

Would you like me to generate the `requirements.txt` as well based on your current pro
