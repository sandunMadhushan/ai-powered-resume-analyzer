# AI-Powered Resume Analyzer with ATS Scoring

![Resume Analyzer](https://img.shields.io/badge/Resume%20Analyzer-AI%20Powered-blue)
![ATS Scoring](https://img.shields.io/badge/ATS%20Score-0--100-green)
![License](https://img.shields.io/badge/License-MIT-green)
![Flask](https://img.shields.io/badge/Flask-3.0.2-red)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-lightgrey)
![Responsive](https://img.shields.io/badge/Design-Responsive-orange)

A sophisticated web application that utilizes advanced AI to analyze resumes and provide **ATS (Applicant Tracking System) compatibility scores** along with detailed, constructive feedback to help job seekers enhance their CVs and increase their chances of passing automated screening systems.

![image](https://github.com/user-attachments/assets/c3017e15-f496-4de1-9810-438052ed5654)

<div align="center">

[![Live Demo](https://img.shields.io/badge/✨_Live_Demo-Click_Here-2ea44f?style=for-the-badge)](https://resume.madhushan.me/)

> **⚠️ Note:** The site may take up to **50 seconds** if inactive

</div>

## 🚀 Features

### 🎯 **ATS Compatibility Scoring**

- **ATS Score (0-100)**: Get a comprehensive score based on how well your resume performs with Applicant Tracking Systems
- **Score Breakdown**: Detailed analysis across 5 key criteria:
  - **Keywords (25 pts)**: Industry-specific keyword usage and relevance
  - **Formatting (20 pts)**: Clean, ATS-parseable layout and structure
  - **Experience (25 pts)**: Clear job titles, companies, dates, and achievements
  - **Skills (20 pts)**: Relevant technical and soft skills presentation
  - **Education (10 pts)**: Clear education details and formatting
- **Visual Dashboard**: Color-coded score display with progress bars and detailed breakdown
- **Actionable Improvements**: Specific suggestions to boost your ATS compatibility score

### 🤖 **AI-Powered Analysis**

- **Smart Resume Review**: Leverages OpenAI's GPT models to provide human-like feedback
- **Comprehensive Feedback**: Analyzes multiple resume sections including education, work experience, skills, and more
- **Strengths & Areas for Improvement**: For each section, identifies what's working well and what could be enhanced
- **Industry Best Practices**: Recommendations based on current hiring trends and standards

### 💻 **User Experience**

- **Modern, Responsive UI**: Beautiful interface with gradient designs that works on all devices
- **Real-time Processing**: Fast analysis with elegant loading animations
- **Visual Feedback**: Color-coded results and intuitive progress indicators
- **Error Handling**: Robust error management with appropriate user feedback
- **Mobile Optimized**: Full functionality across desktop, tablet, and mobile devices

## 💻 Technologies Used

### **Backend & AI**

- **Python 3.9+**: Core application language
- **Flask 3.0.2**: Lightweight web framework
- **OpenAI GPT Models**: Advanced AI analysis engine
- **PDFMiner**: Robust PDF text extraction

### **Frontend & UI**

- **HTML5 & CSS3**: Modern web standards
- **JavaScript ES6+**: Interactive user experience
- **Responsive Design**: Mobile-first approach
- **CSS Grid & Flexbox**: Advanced layouts
- **Custom Animations**: Smooth user interactions

### **Features & Analysis**

- **ATS Scoring Algorithm**: 5-category evaluation system
- **Real-time Processing**: Instant feedback delivery
- **Visual Dashboard**: Interactive score breakdown
- **Error Handling**: Robust exception management

### **Deployment & Infrastructure**

- **Render**: Cloud hosting platform
- **Gunicorn**: Production WSGI server
- **Environment Variables**: Secure API key management

## 📋 How It Works

### 🔄 **Simple 4-Step Process**

1. **📄 Upload Your Resume**

   - Upload your resume in PDF format
   - Secure processing with instant file validation

2. **🧠 AI Analysis Engine**

   - Advanced AI analyzes your resume across multiple dimensions
   - ATS compatibility scoring using industry standards
   - Content quality assessment with professional insights

3. **📊 Comprehensive Results**

   - **ATS Score**: Visual dashboard with 0-100 compatibility rating
   - **Score Breakdown**: Detailed analysis of each scoring criteria
   - **Section-by-Section Feedback**: Strengths and improvement areas
   - **Actionable Recommendations**: Specific steps to enhance your resume

4. **🚀 Implement & Improve**
   - Apply suggested improvements to boost your ATS score
   - Increase your chances of passing automated screening
   - Enhance overall resume quality for human reviewers

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

## 🎯 ATS Scoring System

### **What is ATS Compatibility?**

Applicant Tracking Systems (ATS) are software applications used by companies to automatically screen resumes. Our AI-powered ATS scoring system evaluates your resume based on the same criteria these systems use.

### **Scoring Criteria Breakdown**

| Category          | Points | What We Analyze                                                  |
| ----------------- | ------ | ---------------------------------------------------------------- |
| 🔑 **Keywords**   | 25/100 | Industry-specific terms, job-relevant vocabulary, skill mentions |
| 📄 **Formatting** | 20/100 | Clean layout, proper sections, ATS-parseable structure           |
| 💼 **Experience** | 25/100 | Clear job titles, company names, dates, quantified achievements  |
| 🛠️ **Skills**     | 20/100 | Technical skills, soft skills, relevant competencies             |
| 🎓 **Education**  | 10/100 | Degree information, institutions, graduation dates               |

### **Score Interpretation**

- 🟢 **80-100**: **Excellent** - Your resume is highly ATS-friendly
- 🔵 **60-79**: **Good** - Minor improvements can make it even better
- 🟠 **40-59**: **Fair** - Several improvements needed for better compatibility
- 🔴 **0-39**: **Poor** - Significant improvements required

### **Key Benefits**

✅ **Increase Interview Chances**: Better ATS scores = higher chance of human review  
✅ **Industry Standards**: Analysis based on current ATS technology and best practices  
✅ **Actionable Insights**: Specific recommendations to improve each scoring category  
✅ **Visual Feedback**: Easy-to-understand dashboard with progress indicators

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

- ✅ ~~ATS (Applicant Tracking System) compatibility scoring~~ **COMPLETED**
- 🔄 Industry-specific resume analysis and recommendations
- 🎯 Job description matching and customization suggestions
- 📑 Resume template recommendations based on industry
- 📄 Custom PDF report generation with detailed insights
- 👤 User accounts to track resume improvements over time
- 📈 Resume performance analytics and trends
- 🤖 AI-powered resume optimization suggestions
- 🌐 Multi-language resume analysis support

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## 🙌 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 👨‍💻 Authors

- Sandun Madhushan - [sandunMadhushan](https://github.com/sandunMadhushan)

## 🙏 Acknowledgements

- [OpenAI](https://openai.com/) for their powerful API
- [Flask](https://flask.palletsprojects.com/) for the web framework
- [PDFMiner](https://github.com/pdfminer/pdfminer.six) for PDF text extraction

---

Made with ❤️ by [Sandun Madhushan](https://sandun.is-a.dev/)
