#!/usr/bin/env python3
"""
Test script to verify your setup is correct
"""
import os
import sys

print("=" * 60)
print("🔍 AI Job Tracker - Setup Verification")
print("=" * 60)

# Check Python version
python_version = sys.version_info
print(f"\n1. Python Version: {python_version.major}.{python_version.minor}.{python_version.micro}")
if python_version.major >= 3 and python_version.minor >= 8:
    print("   ✅ Python version OK")
else:
    print("   ❌ Python 3.8+ required")

# Check if .env exists
print("\n2. Environment File (.env):")
if os.path.exists('.env'):
    print("   ✅ .env file found")
    with open('.env', 'r') as f:
        content = f.read()
        if 'OPENAI_API_KEY' in content:
            print("   ✅ OPENAI_API_KEY found in .env")
            # Check if it's not the placeholder
            if 'sk-your' not in content and 'sk-proj' in content or 'sk-' in content:
                print("   ✅ API key appears to be set")
            else:
                print("   ⚠️  API key looks like placeholder - please update it")
        else:
            print("   ❌ OPENAI_API_KEY not found in .env")
else:
    print("   ❌ .env file not found")
    print("   📝 Create .env file with: OPENAI_API_KEY=sk-your-key-here")

# Check required packages
print("\n3. Required Packages:")
required_packages = [
    'flask',
    'flask_cors',
    'dotenv',
    'openai',
    'PyPDF2',
    'docx',
    'werkzeug'
]

for package in required_packages:
    try:
        if package == 'dotenv':
            __import__('dotenv')
        elif package == 'docx':
            __import__('docx')
        elif package == 'PyPDF2':
            __import__('PyPDF2')
        else:
            __import__(package)
        print(f"   ✅ {package}")
    except ImportError:
        print(f"   ❌ {package} - run: pip install {package}")

# Check folder structure
print("\n4. Folder Structure:")
folders = ['templates', 'static', 'uploads']
for folder in folders:
    if os.path.exists(folder):
        print(f"   ✅ {folder}/ exists")
    else:
        print(f"   ⚠️  {folder}/ missing - will be auto-created")

# Check required files
print("\n5. Required Files:")
files = {
    'app.py': 'Main application',
    'templates/index.html': 'HTML template',
    'static/app.js': 'JavaScript file',
    'requirements.txt': 'Dependencies'
}

for file, description in files.items():
    if os.path.exists(file):
        print(f"   ✅ {file} ({description})")
    else:
        print(f"   ❌ {file} ({description}) - MISSING!")

print("\n" + "=" * 60)
print("🎯 Setup Check Complete!")
print("=" * 60)

# Final recommendation
missing_critical = not os.path.exists('.env') or not os.path.exists('app.py')
if missing_critical:
    print("\n❌ Critical files missing. Please ensure all files are in place.")
else:
    print("\n✅ Setup looks good! Try running: python app.py")
print("=" * 60)