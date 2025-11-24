#!/usr/bin/env python3
"""
Startup script with better error handling and diagnostics
"""
import os
import sys

def check_environment():
    """Check if environment is properly set up"""
    issues = []
    
    # Check .env file
    if not os.path.exists('.env'):
        issues.append("❌ .env file not found")
        print("\n⚠️  Creating .env file from template...")
        if os.path.exists('.env.example'):
            import shutil
            shutil.copy('.env.example', '.env')
            print("✅ .env file created. Please edit it and add your OpenAI API key!")
            issues.append("⚠️  Please edit .env and add your OPENAI_API_KEY")
        else:
            print("❌ .env.example not found. Creating basic .env...")
            with open('.env', 'w') as f:
                f.write("OPENAI_API_KEY=sk-your-openai-api-key-here\n")
                f.write("SECRET_KEY=change-this-to-random-string\n")
                f.write("FLASK_ENV=development\n")
                f.write("FLASK_DEBUG=True\n")
            print("✅ .env file created. Please edit it and add your OpenAI API key!")
            issues.append("⚠️  Please edit .env and add your OPENAI_API_KEY")
    
    # Check folders
    for folder in ['templates', 'static', 'uploads']:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"✅ Created {folder}/ directory")
    
    # Check critical files
    if not os.path.exists('app.py'):
        issues.append("❌ app.py not found")
    if not os.path.exists('templates/index.html'):
        issues.append("❌ templates/index.html not found")
    if not os.path.exists('static/app.js'):
        issues.append("❌ static/app.js not found")
    
    return issues

def main():
    print("=" * 70)
    print("🚀 AI Job Tracker - Starting Up")
    print("=" * 70)
    
    # Check environment
    issues = check_environment()
    
    if issues:
        print("\n⚠️  Issues detected:")
        for issue in issues:
            print(f"  {issue}")
        
        critical = any('❌' in issue for issue in issues)
        if critical:
            print("\n❌ Cannot start due to critical issues. Please fix them first.")
            print("\nQuick fixes:")
            print("  1. Ensure all project files are in place")
            print("  2. Create/edit .env file with your OpenAI API key")
            print("  3. Run: pip install -r requirements.txt")
            sys.exit(1)
        else:
            print("\n⚠️  Warning issues found, but continuing...")
    
    # Try to import and run Flask app
    try:
        print("\n📦 Loading application...")
        from app import app
        
        print("✅ Application loaded successfully!")
        print("\n" + "=" * 70)
        print("🌐 Starting Flask server...")
        print("=" * 70)
        print(f"📍 Local:            http://localhost:5000")
        print(f"📍 Network:          http://127.0.0.1:5000")
        print("=" * 70)
        print("💡 Tip: Press CTRL+C to stop the server")
        print("💡 Tip: If browser doesn't open, manually visit the URL above")
        print("=" * 70 + "\n")
        
        # Run the app
        app.run(
            debug=True,
            host='0.0.0.0',
            port=5000,
            use_reloader=True
        )
        
    except ImportError as e:
        print(f"\n❌ Error importing app: {e}")
        print("\n🔧 Troubleshooting:")
        print("  1. Check if all files exist (app.py, templates/, static/)")
        print("  2. Install dependencies: pip install -r requirements.txt")
        print("  3. Check Python version: python --version (need 3.8+)")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error starting server: {e}")
        print(f"\n🐛 Error details: {type(e).__name__}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Server stopped by user. Goodbye!")
        sys.exit(0)