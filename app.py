# app.py
import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from resume_scorer import extract_text_from_pdf, get_resume_analysis

# Initialize the Flask application
app = Flask(__name__)
# Configure the upload folder and allowed extensions
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create the upload folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    """
    Checks if the uploaded file has a valid extension.
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    """
    Handles the file upload and analysis.
    """
    analysis_result = None
    if request.method == 'POST':
        # Check if the post request has the files and job description
        if 'resume' not in request.files or 'job_description' not in request.form:
            return redirect(request.url)

        resume_file = request.files['resume']
        job_description = request.form['job_description']

        # If the user does not select a file, the browser submits an empty part
        if resume_file.filename == '':
            return redirect(request.url)

        if resume_file and allowed_file(resume_file.filename):
            filename = secure_filename(resume_file.filename)
            resume_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            resume_file.save(resume_path)

            # Extract text from the uploaded resume
            resume_text = extract_text_from_pdf(resume_path)
            
            if "Error" in resume_text:
                analysis_result = resume_text
            else:
                # Get the analysis from the Gemini API
                analysis_result = get_resume_analysis(resume_text, job_description)

            # Clean up the temporary file after processing
            os.remove(resume_path)

    return render_template('index.html', analysis=analysis_result)

if __name__ == '__main__':
    app.run(debug=True)