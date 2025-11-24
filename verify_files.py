#!/usr/bin/env python3
"""
Verify all required files exist and are in correct locations
"""
import os

print("=" * 70)
print("📂 File Structure Verification")
print("=" * 70)

required_files = {
    'app.py': 'Main Flask application',
    'run.py': 'Startup script',
    '.env': 'Environment variables',
    'requirements.txt': 'Python dependencies',
    'templates/index.html': 'Main HTML template',
    'static/app.js': 'JavaScript file'
}

print("\n✅ = File exists")
print("❌ = File MISSING\n")

all_good = True
missing_files = []

for file_path, description in required_files.items():
    exists = os.path.exists(file_path)
    icon = "✅" if exists else "❌"
    print(f"{icon} {file_path:<30} ({description})")
    
    if not exists:
        all_good = False
        missing_files.append(file_path)
        
    # If file exists, show file size
    if exists:
        size = os.path.getsize(file_path)
        if size == 0:
            print(f"   ⚠️  WARNING: File is empty (0 bytes)!")
            all_good = False
        else:
            print(f"   📊 Size: {size:,} bytes")

print("\n" + "=" * 70)

if all_good:
    print("✅ All files present and non-empty!")
    print("\nNext step: Make sure your .env has a valid OPENAI_API_KEY")
else:
    print("❌ MISSING FILES DETECTED!")
    print("\nMissing files:")
    for f in missing_files:
        print(f"  - {f}")
    print("\n💡 Create these files and restart the server.")

print("=" * 70)

# Check if templates/index.html has content
if os.path.exists('templates/index.html'):
    with open('templates/index.html', 'r', encoding='utf-8') as f:
        content = f.read()
        if len(content) < 100:
            print("\n⚠️  WARNING: templates/index.html seems too small!")
            print(f"   Current size: {len(content)} characters")
            print("   It should be several thousand characters.")
        else:
            print(f"\n✅ templates/index.html looks good ({len(content):,} characters)")

# Check if static/app.js has content
if os.path.exists('static/app.js'):
    with open('static/app.js', 'r', encoding='utf-8') as f:
        content = f.read()
        if len(content) < 100:
            print("⚠️  WARNING: static/app.js seems too small!")
            print(f"   Current size: {len(content)} characters")
            print("   It should be several thousand characters.")
        else:
            print(f"✅ static/app.js looks good ({len(content):,} characters)")

print("\n" + "=" * 70)