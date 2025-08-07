import google.generativeai as genai
from dotenv import load_dotenv
import pdfplumber
import os

load_dotenv()
# Configure the Gemini API with your API key from the .env file
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file.
    """
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
    except Exception as e:
        return f"Error extracting text from PDF: {e}"
    return text

def get_resume_analysis(resume_text, job_description):
    """
    Sends the resume text and job description to the Gemini 1.5 Flash model for analysis.
    """
    # Use the correct model name for the Python SDK
    model = genai.GenerativeModel("gemini-1.5-flash-latest")
    
    prompt = f"""
You are a professional resume analyst. Your task is to evaluate a candidate's resume against a specific job description.

Analyze the following resume and job description.
First, provide a score from 1 to 100 on how well the resume matches the job description.
Second, provide a list of concrete suggestions for how the candidate can improve their resume to better align with the job description. Focus on missing keywords, skill gaps, and areas for improvement.
Third, provide a list of general corrections for the resume, such as grammar, formatting, or clarity issues.
Present the output in a clear and well-formatted manner.

Job Description:
---
{job_description}
---

Resume:
---
{resume_text}
---

Provide your analysis in the following structured format:

Resume Score: [Score out of 100]
---
Suggestions for Improvement:
- [Suggestion 1]
- [Suggestion 2]
- [Suggestion 3]
...
---
General Corrections:
- [Correction 1]
- [Correction 2]
...
"""
    
    try:
        # Use the generate_content method to send the prompt to the model
        response = model.generate_content(prompt)
        
        # Check if the response is valid and return the text
        if response and response.text:
            return response.text
        else:
            return "The API returned an empty or invalid response."
    except Exception as e:
        return f"An error occurred while communicating with the Gemini API: {e}"