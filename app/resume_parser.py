import openai
from pdfminer.high_level import extract_text
from io import BytesIO
import os
from dotenv import load_dotenv
import json

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')
print(f"Loaded API key: {openai.api_key[:10]}...")  # Print first 10 chars for debugging

def parse_resume(file):
    # Read the file content into a BytesIO object
    file_content = file.read()
    pdf_file = BytesIO(file_content)
    text = extract_text(pdf_file)
    return text

def analyze_resume(resume_text):
    """Analyze the resume using OpenAI's API"""
    try:
        # Create the prompt for the analysis
        prompt = f"""Analyze this resume and provide detailed feedback in JSON format with the following structure:
        {{
            "feedback": {{
                "overallAssessment": {{
                    "strengths": ["list of key strengths"],
                    "areasForImprovement": ["list of areas to improve"]
                }},
                "educationSection": {{
                    "strengths": ["list of strengths"],
                    "areasForImprovement": ["list of improvements"]
                }},
                "extraCurricularActivities": {{
                    "strengths": ["list of strengths"],
                    "areasForImprovement": ["list of improvements"]
                }},
                "awardsAndAchievements": {{
                    "strengths": ["list of strengths"],
                    "areasForImprovement": ["list of improvements"]
                }},
                "professionalExperience": {{
                    "strengths": ["list of strengths"],
                    "areasForImprovement": ["list of improvements"]
                }},
                "aboutMeSection": {{
                    "strengths": ["list of strengths"],
                    "areasForImprovement": ["list of improvements"]
                }},
                "skillsSection": {{
                    "strengths": ["list of strengths"],
                    "areasForImprovement": ["list of improvements"]
                }}
            }}
        }}

        Resume text:
        {resume_text}

        Provide specific, actionable feedback for each section. Focus on strengths and areas for improvement.
        Keep the response concise but detailed. Ensure the JSON is properly formatted and complete."""

        # Get the analysis from OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a professional resume reviewer. Provide detailed, constructive feedback in JSON format."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=2000
        )

        # Extract the content from the response
        content = response['choices'][0]['message']['content'].strip()
        
        # Try to parse the content as JSON to validate it
        try:
            feedback = json.loads(content)
            return feedback
        except json.JSONDecodeError as e:
            print(f"JSON parsing error: {e}")
            print(f"Raw content: {content}")
            # If JSON parsing fails, try to extract the JSON part from the content
            try:
                # Find the first { and last } to extract the JSON
                start = content.find('{')
                end = content.rfind('}') + 1
                if start >= 0 and end > start:
                    json_str = content[start:end]
                    feedback = json.loads(json_str)
                    return feedback
            except Exception as e:
                print(f"Failed to extract JSON: {e}")
                return {"error": "Failed to parse resume analysis", "raw_content": content}

    except Exception as e:
        print(f"Error in analyze_resume: {e}")
        return {"error": str(e)}
