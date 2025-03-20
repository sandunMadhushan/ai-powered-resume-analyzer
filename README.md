# AI-Powered Resume Analyzer

![Resume Analyzer](https://img.shields.io/badge/Resume%20Analyzer-AI%20Powered-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Flask](https://img.shields.io/badge/Flask-3.0.2-red)
![OpenAI](https://img.shields.io/badge/OpenAI-Powered-lightgrey)

A sophisticated web application that utilizes the power of AI to analyze resumes and provide detailed, constructive feedback to help job seekers enhance their CVs and increase their chances of landing interviews.

![Resume Analyzer Screenshot](https://via.placeholder.com/800x450?text=AI+Resume+Analyzer)

## 🚀 Features

- **AI-Powered Analysis**: Leverages OpenAI's GPT models to provide human-like feedback on your resume
- **Comprehensive Feedback**: Analyzes multiple resume sections including education, work experience, skills, and more
- **Strengths & Areas for Improvement**: For each section, identifies what's working well and what could be enhanced
- **Actionable Suggestions**: Provides specific, constructive recommendations that can be implemented immediately
- **Modern, Responsive UI**: Clean interface that works on desktop and mobile devices
- **Real-time Processing**: Fast analysis with a friendly loading indicator
- **Error Handling**: Robust error management with appropriate user feedback

## 💻 Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **AI**: OpenAI GPT Models
- **PDF Processing**: PDFMiner
- **Deployment**: Compatible with Render, Heroku, and other platforms

## 📋 How It Works

1. Upload your resume in PDF format
2. Our AI analyzes your resume across multiple dimensions
3. Get detailed feedback on each section of your resume
4. Implement the suggestions to improve your chances of landing interviews

## 🔧 Installation & Setup

### Prerequisites

- Python 3.9+
- An OpenAI API key

### Local Development

```bash
# Clone the repository
git clone https://github.com/sandunMadhushan/ai-powered-resume-analyzer.git
cd ai-powered-resume-analyzer

# Set up a virtual environment
python -m venv venv

# Activate virtual environment

# For Windows:
venv\Scripts\activate

# For macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create a .env file and add your OpenAI API key
echo "OPENAI_API_KEY=your_api_key_here" > .env

# Run the application
python run.py
```

Visit `http://localhost:5000` in your browser to use the application.

## 🚀 Deployment

### Deploy to Render

1. Push your code to a Git repository (GitHub, GitLab, etc.)
2. Create a new Web Service on Render
3. Connect your repository
4. Set the following:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn run:app`
   - Add the environment variable: `OPENAI_API_KEY`

## 🔍 Project Structure

```
ai-powered-resume-analyzer/
│
├── app/                    # Main application package
│   ├── __init__.py         # Initialize Flask app
│   ├── routes.py           # Route definitions
│   ├── resume_parser.py    # PDF parsing and AI analysis
│   ├── static/             # Static files
│   │   ├── css/            # CSS styles
│   │   ├── js/             # JavaScript files
│   │   └── img/            # Images
│   └── templates/          # Jinja2 templates
│       ├── base.html       # Base template
│       └── index.html      # Main page
│
├── venv/                   # Virtual environment (not in repo)
├── .env                    # Environment variables (not in repo)
├── .gitignore              # Git ignore file
├── requirements.txt        # Project dependencies
├── run.py                  # Application entry point
└── README.md               # Project documentation
```

## 💡 Future Enhancements

- ATS (Applicant Tracking System) compatibility scoring
- Industry-specific resume analysis
- Job description matching and customization suggestions
- Resume template recommendations
- Custom PDF report generation
- User accounts to track resume improvements over time

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙌 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 👨‍💻 Authors

- Sandun Madhushan - [sandunMadhushan](https://github.com/sandunMadhushan)

## 🙏 Acknowledgements

- [OpenAI](https://openai.com/) for their powerful API
- [Flask](https://flask.palletsprojects.com/) for the web framework
- [PDFMiner](https://github.com/pdfminer/pdfminer.six) for PDF text extraction

---

Made with ❤️ by [Sandun Madhushan](sandun.is-a.dev)
