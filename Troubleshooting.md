# 🔧 Troubleshooting Guide

## Problem: App runs but shows no output / doesn't launch browser

### Quick Fixes (Try these first):

#### **Solution 1: Use the new run.py script**
```bash
python run.py
```
This script has better error handling and diagnostics.

#### **Solution 2: Check if app is actually running**
```bash
# After running python app.py, manually visit:
http://localhost:5000
# or
http://127.0.0.1:5000
```

#### **Solution 3: Check for errors**
```bash
# Run with verbose output
python -u app.py
```

#### **Solution 4: Check if port is already in use**
```powershell
# On Windows PowerShell:
netstat -ano | findstr :5000

# If port is in use, kill the process:
# Get the PID from the output above, then:
taskkill /PID <PID_NUMBER> /F
```

#### **Solution 5: Run the test script first**
```bash
python test_setup.py
```
This will check if everything is configured correctly.

---

## Detailed Diagnostics

### 1. Verify .env file exists and is correct

```bash
# Check if .env exists
dir .env

# View contents (Windows)
type .env

# It should contain:
OPENAI_API_KEY=sk-proj-... (your actual key)
SECRET_KEY=some-random-string
```

### 2. Verify all files are present

Your folder structure should look like this:
```
AI-Powered_Job-Application_Automation/
├── app.py
├── run.py
├── test_setup.py
├── requirements.txt
├── .env
├── .env.example
├── README.md
├── templates/
│   └── index.html
├── static/
│   └── app.js
├── uploads/
└── venv/
```

### 3. Check Python and package versions

```bash
# Check Python version (need 3.8+)
python --version

# Check if Flask is installed
pip show flask

# Check if all packages are installed
pip list
```

### 4. Try running with different options

```bash
# Option A: Using run.py (recommended)
python run.py

# Option B: Direct app.py
python app.py

# Option C: Using Flask CLI
set FLASK_APP=app.py
flask run

# Option D: Specific host and port
python -c "from app import app; app.run(host='127.0.0.1', port=5000, debug=True)"
```

### 5. Check Windows Firewall

Windows might be blocking Flask:
1. Open "Windows Defender Firewall"
2. Click "Allow an app through firewall"
3. Look for Python
4. Ensure both Private and Public are checked

### 6. Try a different port

Edit `app.py` or `run.py` and change:
```python
app.run(debug=True, port=5001)  # Use 5001 instead
```

Then visit: http://localhost:5001

---

## Common Error Messages & Solutions

### "No module named 'flask'"
```bash
pip install -r requirements.txt
```

### "OPENAI_API_KEY not found"
1. Create `.env` file in project root
2. Add: `OPENAI_API_KEY=sk-your-key-here`
3. Make sure there are no extra spaces

### "Address already in use"
```bash
# Kill process on port 5000
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

### "Template not found"
```bash
# Verify folder structure
dir templates
dir templates\index.html
```

### "Permission denied"
```bash
# Run as administrator or check folder permissions
```

---

## Still Not Working?

### Manual Step-by-Step Test

1. **Test Python**:
```bash
python -c "print('Python works!')"
```

2. **Test Flask Import**:
```bash
python -c "import flask; print('Flask version:', flask.__version__)"
```

3. **Test OpenAI**:
```bash
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print('API Key loaded:', bool(os.getenv('OPENAI_API_KEY')))"
```

4. **Test app import**:
```bash
python -c "from app import app; print('App loaded successfully')"
```

5. **Test minimal Flask**:
Create `test_flask.py`:
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Flask is working!'

if __name__ == '__main__':
    print("Starting test server on http://localhost:5000")
    app.run(debug=True, port=5000)
```

Run it:
```bash
python test_flask.py
```

---

## Alternative: Use Flask CLI

```bash
# Set environment variables
set FLASK_APP=app.py
set FLASK_ENV=development
set FLASK_DEBUG=1

# Run Flask
flask run --host=0.0.0.0 --port=5000
```

---

## Check Logs

Look for error messages in:
1. Terminal output
2. Windows Event Viewer (if app crashes)
3. Create a log file:

```python
# Add to app.py at the top
import logging
logging.basicConfig(level=logging.DEBUG)
```

---

## Getting More Help

If still stuck, provide:
1. Output of `python --version`
2. Output of `pip list`
3. Output of `python test_setup.py`
4. Any error messages from terminal
5. Screenshot of folder structure

---

## Quick Reference Commands

```bash
# Activate venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run tests
python test_setup.py

# Start app (recommended)
python run.py

# Start app (alternative)
python app.py

# Check what's running on port 5000
netstat -ano | findstr :5000

# Deactivate venv
deactivate
```