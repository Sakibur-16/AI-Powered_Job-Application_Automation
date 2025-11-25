# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Real job board integrations (LinkedIn, Indeed APIs)
- Email notifications for application deadlines
- Interview preparation features
- Resume optimization suggestions
- Analytics dashboard

---

## [1.0.0] - 2024-11-26

### 🎉 Initial Release

#### Added
- **AI Resume Parser**
  - Upload resume files (PDF, DOCX, DOC, TXT)
  - Automatic extraction of name, email, phone, skills, experience, and education
  - Support for multiple file formats using PyPDF2 and python-docx

- **Intelligent Job Search**
  - AI-powered job listing generation using OpenAI GPT-4
  - Custom job search based on user's skills and keywords
  - Automatic job ranking with fit scores (0-100%)
  - Detailed explanations for why each job matches user's profile

- **AI Cover Letter Generator**
  - Personalized cover letter creation for each job
  - Highlights relevant skills and experience
  - Professional 3-paragraph format
  - Copy to clipboard functionality

- **Application Tracker**
  - Notion-style Kanban board with 5 stages:
    - Applied
    - Screening
    - Interview
    - Offer
    - Rejected
  - Drag-and-drop status updates
  - Application count per stage
  - Persistent storage in browser localStorage

- **User Interface**
  - Modern, responsive design using Tailwind CSS
  - Dark mode with theme persistence
  - Smooth transitions and animations
  - Mobile-friendly layout
  - Three main tabs: Resume, Find Jobs, Applications

- **Privacy & Security**
  - All user data stored locally in browser
  - Secure API key storage in .env file
  - No external database required
  - Temporary file cleanup after resume processing

- **Documentation**
  - Comprehensive README with installation guide
  - Detailed SETUP.md for step-by-step configuration
  - TROUBLESHOOTING.md for common issues
  - CONTRIBUTING.md for contributors
  - Code examples and screenshots

- **Development Tools**
  - `run.py` - Enhanced startup script with diagnostics
  - `test_setup.py` - Setup verification script
  - `verify_files.py` - File structure checker
  - `start.bat` - Windows quick start script
  - `.env.example` - Environment template

#### Technical Details
- **Backend**: Flask 3.0.0, Python 3.8+
- **AI**: OpenAI GPT-4o integration
- **Frontend**: HTML5, Tailwind CSS, Vanilla JavaScript
- **File Processing**: PyPDF2, python-docx
- **Storage**: Browser localStorage, Python-dotenv

---

## Release Notes Template (For Future Versions)

### [X.Y.Z] - YYYY-MM-DD

#### Added
- New features

#### Changed
- Changes in existing functionality

#### Deprecated
- Soon-to-be removed features

#### Removed
- Removed features

#### Fixed
- Bug fixes

#### Security
- Security improvements

---

## Version History

### Version Naming Convention
- **Major (X.0.0)**: Breaking changes, major new features
- **Minor (1.X.0)**: New features, backward compatible
- **Patch (1.0.X)**: Bug fixes, minor improvements

### Changelog Links
- [Unreleased]: https://github.com/Sakibur-16/AI-Powered_Job-Application_Automation
- [1.0.0]: https://github.com/Sakibur-16/AI-Powered_Job-Application_Automation
