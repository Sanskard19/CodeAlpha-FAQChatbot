# CodeAlpha-FAQChatbot

An FAQ chatbot project built for academic submission using Python, Flask, HTML, CSS, and JavaScript. The chatbot matches a user's question with the most similar FAQ using NLP preprocessing, TF-IDF vectorization, and cosine similarity.

## Project Objective

Build a chatbot that:
- Collects FAQs and their answers.
- Preprocesses text using NLP.
- Matches user input with the most similar FAQ.
- Displays the best answer and related questions.
- Provides a simple web chat interface.

## Domain Chosen

This project uses a fictional SaaS support domain called **NexusAI**.

## Project Structure

```text
CodeAlpha-FAQChatbot/
├── app.py
├── chatbot.py
├── preprocess.py
├── requirements.txt
├── README.md
├── .gitignore
├── data/
│   ├── faqs.json
│   └── faqs.csv
├── scripts/
│   └── run_steps.txt
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── app.js
└── templates/
    └── index.html
```

## Technologies Used

- Python
- Flask
- NLTK
- scikit-learn
- HTML
- CSS
- JavaScript

## How It Works

### 1. FAQ Collection
A dataset of frequently asked questions and answers is stored in JSON and CSV format.

### 2. NLP Preprocessing
The `preprocess.py` file:
- Converts text to lowercase
- Removes punctuation
- Tokenizes text using NLTK
- Removes stopwords

### 3. Similarity Matching
The `chatbot.py` file:
- Uses `TfidfVectorizer` to convert FAQ questions into vectors
- Uses `cosine_similarity` to compare user input with stored FAQs
- Returns the best answer and top related questions

### 4. Chat UI
The Flask app serves a browser-based chat interface where users can ask questions.

## Setup Instructions

### 1. Create virtual environment (recommended)
```bash
python -m venv venv
```

### 2. Activate virtual environment
Windows:
```bash
venv\Scripts\activate
```

Linux/macOS:
```bash
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run preprocessing
```bash
python preprocess.py
```

### 5. Start the app
```bash
python app.py
```

### 6. Open in browser
```text
http://127.0.0.1:5000
```

## Sample Questions

- What is NexusAI?
- How do I reset my password?
- Does NexusAI have an API?
- What are the pricing plans?
- Is my data secure?

## Submission Notes

For GitHub submission:
- Upload the full project folder.
- Keep the repository public.
- Add screenshots of the chatbot UI in the repo if possible.
- Add your demo video link in the README after recording it.

## Future Improvements

- Use spaCy or sentence transformers for better semantic matching
- Add chat history storage
- Deploy the app online
- Add voice input
