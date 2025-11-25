# 🚀 AI-Powered Job Application Tracker

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

**A privacy-focused, AI-powered job application tracker that helps you land your dream job faster.**

[Features](#-features) • [Demo](#-demo) • [Installation](#-installation) • [Usage](#-usage) • [Contributing](#-contributing)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Demo](#-demo)
- [Screenshots](#-screenshots)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [API Costs](#-api-costs)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)
- [Support](#-support)

---

## 🎯 Overview

**AI Job Tracker** is an intelligent job application management system that leverages OpenAI's GPT-4 to streamline your job search process. Upload your resume, let AI extract your skills, search for matching jobs, generate tailored cover letters, and track applications through a beautiful Kanban board interface.

### Why This Project?

- 🔒 **Privacy First**: All data stored locally, no external databases
- 🤖 **AI-Powered**: Smart resume parsing, job matching, and cover letter generation
- 🎨 **Beautiful UI**: Modern design with dark mode support
- 📊 **Application Tracking**: Notion-style Kanban board to manage your pipeline
- 💰 **Cost-Effective**: Uses your own OpenAI API key, only pay for what you use

---

## ✨ Features

### 🎯 Core Functionality

| Feature | Description |
|---------|-------------|
| **AI Resume Parser** | Upload resume (PDF/DOCX/TXT) and automatically extract skills, experience, and education |
| **Intelligent Job Search** | AI generates realistic job listings tailored to your profile |
| **Smart Job Ranking** | Get 0-100% fit scores with explanations for each job |
| **AI Cover Letter Generator** | Create personalized cover letters highlighting relevant experience |
| **Application Tracker** | Kanban board with 5 stages: Applied → Screening → Interview → Offer → Rejected |

### 🎨 User Experience

- ✅ **Dark Mode**: Toggle between light/dark themes with persistence
- ✅ **Responsive Design**: Works on desktop, tablet, and mobile
- ✅ **Real-time Updates**: Instant UI updates without page refreshes
- ✅ **Local Storage**: Resume and application data persists in browser
- ✅ **File Support**: PDF, DOCX, DOC, and TXT file uploads

### 🔒 Privacy & Security

- ✅ **Local-First**: All data stored in browser localStorage
- ✅ **Secure API Key**: Stored in `.env` file (server-side only)
- ✅ **No Database**: No external servers or databases required
- ✅ **Self-Hosted**: Deploy anywhere you want

---

## 🎬 Demo

### Quick Start Video
[Add your demo video link here]

### Live Demo
[Add your deployed demo link here - optional]

---

## 📸 Screenshots

<div align="center">

### Resume Upload
<img src="screenshots/resume-upload.png" width="800" alt="Resume Upload">

### Job Search
<img src="screenshots/job-search.png" width="800" alt="Job Search">

### Application Tracker
<img src="screenshots/tracker.png" width="800" alt="Application Tracker">

### Dark Mode
<img src="screenshots/dark-mode.png" width="800" alt="Dark Mode">

</div>

---

## 🛠️ Tech Stack

### Backend
- **Python 3.8+** - Core language
- **Flask 3.0.0** - Web framework
- **OpenAI GPT-4** - AI capabilities
- **python-dotenv** - Environment management

### Frontend
- **HTML5** - Structure
- **Tailwind CSS** - Styling
- **Vanilla JavaScript** - Interactivity
- **LocalStorage API** - Data persistence

### File Processing
- **PyPDF2** - PDF parsing
- **python-docx** - DOCX parsing

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

### Step 1: Clone Repository

```bash
git clone https://github.com/yourusername/ai-job-tracker.git
cd ai-job-tracker
```

### Step 2: Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Set Up Environment Variables

```bash
# Copy the example file
cp .env.example .env

# Edit .env and add your OpenAI API key
# Use any text editor (VS Code, Notepad++, etc.)
```

Your `.env` file should look like this:

```env
OPENAI_API_KEY=sk-proj-your-actual-api-key-here
SECRET_KEY=your-random-secret-key-change-this
FLASK_ENV=development
FLASK_DEBUG=True
```
### MUST USE API KEY FOR GETTING RESULTS
### Step 5: Run the Application

```bash
# Option 1: Using run.py (recommended)
python run.py

# Option 2: Direct app.py
python app.py

# Option 3: Windows batch file
start.bat
```

### Step 6: Open in Browser

Navigate to: **http://localhost:5000**

---

## ⚙️ Configuration

### OpenAI Model Selection

Edit `app.py` to change the AI model:

```python
# Current: GPT-4o (most capable)
model="gpt-4o"

# Alternative: GPT-4o-mini (faster, cheaper)
model="gpt-4o-mini"

# Alternative: GPT-3.5-turbo (fastest, most economical)
model="gpt-3.5-turbo"
```

### Adjusting AI Temperature

Control creativity vs. consistency:

```python
# More creative (0.7-1.0)
temperature=0.9

# More consistent (0.1-0.3) - recommended for parsing
temperature=0.3
```

### Changing Port

In `app.py` or `run.py`:

```python
app.run(debug=True, port=5001)  # Change to any available port
```

---

## 📖 Usage

### 1. Upload Resume

1. Click the **Resume** tab
2. Upload your resume (PDF, DOCX, DOC, or TXT)
3. AI automatically extracts:
   - Personal information (name, email, phone)
   - Skills and technologies
   - Work experience
   - Education

### 2. Search for Jobs

1. Navigate to **Find Jobs** tab
2. Enter keywords (e.g., "Software Engineer Python")
3. Click **Search**
4. Review AI-generated job listings ranked by fit score
5. Each job shows:
   - Fit score (0-100%)
   - Why it matches your profile
   - Company details
   - Requirements

### 3. Generate Cover Letters

1. Click **Generate Cover Letter** on any job
2. AI creates a personalized 3-paragraph letter
3. Copy to clipboard or use directly

### 4. Track Applications

1. Click **Mark as Applied** to add to tracker
2. Go to **Applications** tab
3. View Kanban board with 5 stages
4. Update status as you progress:
   - **Applied** → Interview scheduled
   - **Screening** → Phone screen
   - **Interview** → On-site/technical
   - **Offer** → Received offer
   - **Rejected** → Not moving forward

### 5. Dark Mode

- Click moon/sun icon in top-right corner
- Preference is saved automatically

---

## 📁 Project Structure

```
ai-job-tracker/
├── app.py                      # Flask backend with OpenAI integration
├── run.py                      # Startup script with diagnostics
├── test_setup.py               # Setup verification script
├── verify_files.py             # File structure checker
├── start.bat                   # Windows quick start script
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables (create this)
├── .env.example                # Environment template
├── .gitignore                  # Git ignore rules
├── README.md                   # This file
├── SETUP.md                    # Detailed setup guide
├── TROUBLESHOOTING.md          # Common issues and fixes
├── LICENSE                     # MIT License
│
├── templates/
│   └── index.html              # Main HTML template
│
├── static/
│   └── app.js                  # Frontend JavaScript
│
├── uploads/                    # Temporary resume storage
│
├── screenshots/                # UI screenshots
│   ├── resume-upload.png
│   ├── job-search.png
│   ├── tracker.png
│   └── dark-mode.png
│
└── docs/                       # Additional documentation
    ├── API.md                  # API documentation
    ├── CONTRIBUTING.md         # Contribution guidelines
    └── DEPLOYMENT.md           # Deployment guide
```

---


**Monthly Estimate:**
- Light use (10-20 applications): ~$2-5
- Moderate use (50-100 applications): ~$10-20
- Heavy use (200+ applications): ~$30-50

💡 **Pro Tip**: Switch to GPT-4o-mini to reduce costs by ~60%

---

## 🗺️ Roadmap

### Phase 1: Core Features ✅
- [x] Resume upload and AI parsing
- [x] AI job search and ranking
- [x] Cover letter generation
- [x] Application tracking
- [x] Dark mode

### Phase 2: Enhancements 🚧
- [ ] Real job board integrations (LinkedIn, Indeed)
- [ ] Email notifications for deadlines
- [ ] Interview preparation features
- [ ] Resume optimization suggestions
- [ ] Analytics dashboard

### Phase 3: Advanced Features 🔮
- [ ] Browser extension
- [ ] Mobile app (React Native)
- [ ] Team collaboration features
- [ ] AI interview coach
- [ ] Salary negotiation assistant

### Community Requests 💡
- [ ] Multi-language support
- [ ] Export to PDF/CSV
- [ ] Calendar integration
- [ ] Chrome extension for one-click apply

---

## 🤝 Contributing

We love contributions! Here's how you can help:

### Ways to Contribute

1. 🐛 **Report Bugs**: Open an issue with detailed reproduction steps
2. 💡 **Suggest Features**: Share your ideas in discussions
3. 📖 **Improve Docs**: Fix typos, add examples, clarify instructions
4. 🔧 **Submit PRs**: Fix bugs or implement new features

### Development Setup

```bash
# Fork the repo and clone your fork
git clone https://github.com/Sakibur-16/AI-Powered_Job-Application_Automation.git

# Create a feature branch
git checkout -b feature/amazing-feature

# Make your changes and commit
git commit -m "Add amazing feature"

# Push to your fork
git push origin feature/amazing-feature

# Open a Pull Request
```

### Code Guidelines

- Follow PEP 8 for Python code
- Use meaningful variable names
- Add comments for complex logic
- Test your changes before submitting
- Update documentation as needed

### Pull Request Process

1. Ensure all tests pass
2. Update README if needed
3. Add screenshots for UI changes
4. Describe your changes in detail
5. Link related issues

See [CONTRIBUTING.md](docs/CONTRIBUTING.md) for detailed guidelines.

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

---

## 🆘 Support

### Documentation

- 📖 [Setup Guide](SETUP.md)
- 🔧 [Troubleshooting](TROUBLESHOOTING.md)
- 🚀 [Deployment Guide](docs/DEPLOYMENT.md)
- 🔌 [API Documentation](docs/API.md)

### Get Help

- 💬 [GitHub Discussions](https://github.com/yourusername/ai-job-tracker/discussions)
- 🐛 [Report a Bug](https://github.com/yourusername/ai-job-tracker/issues/new?template=bug_report.md)
- 💡 [Request a Feature](https://github.com/yourusername/ai-job-tracker/issues/new?template=feature_request.md)

### Community

- 🌟 Star this repo if you find it helpful
- 🐦 Follow us on Twitter: [@your_handle]
- 💼 Connect on LinkedIn: [Your Profile]

---

## 🙏 Acknowledgments

- **OpenAI** for the amazing GPT-4 API
- **Flask** team for the excellent web framework
- **Tailwind CSS** for the beautiful utility-first CSS
- All contributors who helped make this project better

---

## 📊 Stats

![GitHub Stars](https://img.shields.io/github/stars/yourusername/ai-job-tracker?style=social)
![GitHub Forks](https://img.shields.io/github/forks/yourusername/ai-job-tracker?style=social)
![GitHub Issues](https://img.shields.io/github/issues/yourusername/ai-job-tracker)
![GitHub Pull Requests](https://img.shields.io/github/issues-pr/yourusername/ai-job-tracker)

---

## 🔗 Links

- **Live Demo**: [demo.yoursite.com]
- **Documentation**: [docs.yoursite.com]
- **Blog Post**: [blog.yoursite.com/ai-job-tracker]
- **Video Tutorial**: [youtube.com/watch?v=...]

---

<div align="center">

**Made with ❤️ by [Your Name](https://github.com/yourusername)**

**If this project helped you land a job, consider [buying me a coffee](https://buymeacoffee.com/yourusername)! ☕**

[⬆ Back to Top](#-ai-powered-job-application-tracker)

</div>