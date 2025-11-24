# app.py
from flask import Flask, render_template, request, jsonify, session
from flask_cors import CORS
import os
from dotenv import load_dotenv
import openai
import json
from datetime import datetime
import PyPDF2
import docx
from werkzeug.utils import secure_filename
import sys

# Load environment variables
load_dotenv()

# Check for API key
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    print("⚠️  WARNING: OPENAI_API_KEY not found in .env file!")
    print("Please create a .env file with your OpenAI API key")
    print("Example: OPENAI_API_KEY=sk-your-key-here")
else:
    print(f"✅ OpenAI API Key loaded (starts with: {api_key[:10]}...)")

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'your-secret-key-change-this')
CORS(app)

# OpenAI Configuration
openai.api_key = api_key

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'doc', 'docx'}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    return '\n'.join([paragraph.text for paragraph in doc.paragraphs])

def extract_text_from_file(file_path):
    ext = file_path.rsplit('.', 1)[1].lower()
    if ext == 'pdf':
        return extract_text_from_pdf(file_path)
    elif ext == 'docx':
        return extract_text_from_docx(file_path)
    else:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()

def call_openai(messages, temperature=0.7):
    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            temperature=temperature,
            max_tokens=2000
        )
        return response.choices[0].message.content
    except Exception as e:
        raise Exception(f"OpenAI API Error: {str(e)}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload-resume', methods=['POST'])
def upload_resume():
    if 'resume' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['resume']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        try:
            # Extract text from file
            text = extract_text_from_file(file_path)
            
            # Call OpenAI to extract information
            prompt = f"""Extract key information from this resume and return ONLY a JSON object with no markdown formatting:
{{
  "name": "full name",
  "email": "email",
  "phone": "phone",
  "skills": ["skill1", "skill2", ...],
  "experience": ["job title at company", ...],
  "education": ["degree from school", ...],
  "summary": "brief professional summary"
}}

Resume text:
{text}"""
            
            response = call_openai([{"role": "user", "content": prompt}], temperature=0.3)
            parsed = json.loads(response.replace('```json', '').replace('```', '').strip())
            
            resume_data = {
                'name': parsed.get('name'),
                'email': parsed.get('email'),
                'phone': parsed.get('phone'),
                'summary': parsed.get('summary'),
                'experience': parsed.get('experience', []),
                'education': parsed.get('education', []),
                'skills': parsed.get('skills', []),
                'rawText': text,
                'uploadedAt': datetime.now().isoformat()
            }
            
            # Store in session
            session['resume'] = resume_data
            
            # Clean up uploaded file
            os.remove(file_path)
            
            return jsonify(resume_data)
        
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    return jsonify({'error': 'Invalid file type'}), 400

@app.route('/search-jobs', methods=['POST'])
def search_jobs():
    data = request.json
    query = data.get('query')
    skills = data.get('skills', [])
    
    if not query:
        return jsonify({'error': 'Query is required'}), 400
    
    try:
        # Generate sample jobs
        prompt = f"""Generate 8 realistic job listings for someone with these skills: {', '.join(skills)}
Search query: {query}

Return ONLY a JSON array with no markdown:
[{{
  "id": "unique-id",
  "title": "Job Title",
  "company": "Company Name",
  "location": "City, State/Remote",
  "salary": "$XX,000 - $XX,000",
  "description": "Job description...",
  "requirements": ["req1", "req2", ...],
  "postedDate": "2024-11-XX",
  "url": "https://example.com/job"
}}]"""
        
        response = call_openai([{"role": "user", "content": prompt}])
        jobs = json.loads(response.replace('```json', '').replace('```', '').strip())
        
        # Rank jobs
        ranked_jobs = rank_jobs(jobs, skills)
        
        return jsonify(ranked_jobs)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def rank_jobs(jobs, skills):
    try:
        prompt = f"""Rank these jobs by fit for someone with skills: {', '.join(skills)}

Jobs: {json.dumps(jobs)}

Return ONLY a JSON array with jobs sorted by fit (best first), each with a "fitScore" (0-100) and "fitReason":
[{{
  ...job,
  "fitScore": 85,
  "fitReason": "Strong match because..."
}}]"""
        
        response = call_openai([{"role": "user", "content": prompt}], temperature=0.3)
        return json.loads(response.replace('```json', '').replace('```', '').strip())
    except:
        return [{'fitScore': 50, 'fitReason': 'Unable to calculate fit', **job} for job in jobs]

@app.route('/generate-cover-letter', methods=['POST'])
def generate_cover_letter():
    data = request.json
    job = data.get('job')
    resume = session.get('resume')
    
    if not resume:
        return jsonify({'error': 'Resume not found'}), 400
    
    try:
        prompt = f"""Write a professional, tailored cover letter for this job application:

Applicant: {resume['name']}
Skills: {', '.join(resume['skills'])}
Experience: {'; '.join(resume['experience'])}

Job Title: {job['title']}
Company: {job['company']}
Requirements: {', '.join(job['requirements'])}
Description: {job['description']}

Write a compelling 3-paragraph cover letter that highlights relevant skills and experience. Make it professional but personable."""
        
        response = call_openai([{"role": "user", "content": prompt}])
        return jsonify({'coverLetter': response})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("=" * 60)
    print("🚀 AI Job Tracker is starting...")
    print("=" * 60)
    print(f"📍 Server running at: http://localhost:5000")
    print(f"📍 Or try: http://127.0.0.1:5000")
    print("=" * 60)
    print("Press CTRL+C to quit")
    print("=" * 60)
    app.run(debug=True, port=5000, host='0.0.0.0')