# PDF Question Generator

A powerful tool that takes a PDF file as input, extracts its content, generates questions, and allows users to download the questions as a CSV file. Built using **LangChain** for intelligent text processing and question generation.

---

## Features

- **PDF Input:** Upload any PDF document and extract its text content.
- **Question Generation:** Automatically generates subjective type questions from the PDF content using LangChain.
- **CSV Export:** Download the generated questions as a CSV file for easy use.
- **User-Friendly Interface:** Simple, straightforward interface for uploading PDFs and downloading questions.

---

## How It Works

1. **PDF Processing:**  
   The project reads the uploaded PDF file and extracts its text content.

2. **Question Generation:**  
   Using **LangChain**, the extracted text is processed to generate meaningful questions and answers.

3. **CSV Export:**  
   All questions and options are formatted into a CSV file that the user can download.

---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Lagan-garg10/question-creator/
cd question-creator
pip install -r requirements.txt
python app.py