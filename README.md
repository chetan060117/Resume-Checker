# AI-Powered Resume Analyzer
An intelligent web application that analyzes a resume against a job description, providing a matching score, actionable feedback, and general corrections using the power of the Google Gemini API.

<img width="1747" height="889" alt="image" src="https://github.com/user-attachments/assets/a8ce849b-6b21-4832-acde-3bcf62b46a35" />


# Description
In today's competitive job market, tailoring your resume to a specific job description is crucial. This tool automates and enhances that process. Users can upload their resume in PDF format and paste a job description. The backend, powered by Flask and Google's Gemini 1.5 Flash model, performs a detailed analysis and presents a comprehensive report, helping candidates improve their application's quality and relevance.

# Key Features
Resume vs. Job Description Matching: Get a percentage score indicating how well your resume aligns with the target job.

Targeted Improvement Suggestions: Receive concrete advice on how to better tailor your resume, including missing keywords and skill gaps.

General Resume Corrections: Identifies and suggests fixes for common issues related to grammar, formatting, and clarity.

Simple Web Interface: An easy-to-use interface for uploading files and viewing the analysis.

Direct PDF Processing: Extracts text directly from uploaded PDF resumes.

# Technology Stack
Backend: Python, Flask

AI Model: Google Gemini 1.5 Flash

PDF Text Extraction: pdfplumber

API Client: google-generativeai

Frontend: HTML, CSS

Environment Variables: python-dotenv

# Setup and Installation
Follow these steps to run the project on your local machine.

1. Prerequisites
Python 3.7+

A Google Gemini API Key. You can obtain one from the Google AI Studio.

2. Clone the Repository
Bash

git clone https://github.com/
cd resume-analyzer
3. Create a Virtual Environment
It's recommended to use a virtual environment to manage project dependencies.

On macOS/Linux:

Bash

python3 -m venv venv
source venv/bin/activate
On Windows:

Bash

python -m venv venv
venv\Scripts\activate
4. Install Dependencies
Create a requirements.txt file with the following content:

Plaintext

Flask
google-generativeai
pdfplumber
python-dotenv
werkzeug
Then, install the required packages:

Bash

pip install -r requirements.txt
5. Set Up Environment Variables
Create a file named .env in the root directory of your project and add your Google Gemini API key:

GEMINI_API_KEY="YOUR_API_KEY_HERE"
Replace "YOUR_API_KEY_HERE" with your actual API key.

6. Run the Application
Start the Flask development server:

Bash

flask run
Or, run the app.py script directly:

Bash

python app.py
The application will be available at http://127.0.0.1:5000.

How to Use
Open your web browser and navigate to http://127.0.0.1:5000.

Click the "Choose File" button to upload your resume in PDF format.

Paste the entire job description into the text area.

Click the "Analyze" button.

The page will reload with the analysis results, including the score, improvement suggestions, and general corrections.

# File Structure
.
├── app.py              # Main Flask application, handles routing and file uploads

├── resume_scorer.py    # Core logic for PDF extraction and Gemini API communication

├── templates/

│   └── index.html      # Frontend HTML template

├── uploads/            # Temporary folder for storing uploaded resumes (auto-generated)

├── .env                # Stores environment variables (e.g., API key)

├── requirements.txt    # Lists all Python dependencies

└── README.md           # You are here!
Contributing
Contributions are welcome! If you have suggestions for improvements or want to add new features, please feel free to fork the repository and submit a pull request.
