import os
from pdfminer.high_level import extract_text
from io import BytesIO
from dotenv import load_dotenv
import json
import pkg_resources

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
api_key = os.getenv('OPENAI_API_KEY')
print(f"Loaded API key: {api_key[:10]}...")  # Print first 10 chars for debugging

# Check OpenAI version to use correct client
openai_version = pkg_resources.get_distribution("openai").version
is_new_version = int(openai_version.split('.')[0]) >= 1

if is_new_version:
    # New OpenAI client (v1.0.0+)
    from openai import OpenAI
    client = OpenAI(api_key=api_key)
else:
    # Old OpenAI client (v0.28 or earlier)
    import openai
    openai.api_key = api_key

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

        messages = [
            {"role": "system", "content": "You are a professional resume reviewer. Provide detailed, constructive feedback in JSON format."},
            {"role": "user", "content": prompt}
        ]

        try:
            # Use the appropriate client based on version
            if is_new_version:
                # New OpenAI API (v1.0.0+)
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=messages,
                    temperature=0.7,
                    max_tokens=2000
                )
                content = response.choices[0].message.content.strip()
            else:
                # Old OpenAI API (v0.28 or earlier)
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=messages,
                    temperature=0.7,
                    max_tokens=2000
                )
                content = response['choices'][0]['message']['content'].strip()
        except Exception as api_error:
            print(f"API error: {api_error}")
            return {"error": str(api_error)}
        
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
