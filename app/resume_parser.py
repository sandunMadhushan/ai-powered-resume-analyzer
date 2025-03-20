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
    prompt = f"Analyze this resume:\n\n{resume_text}\n\nProvide feedback in JSON format."
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a professional resume analyzer. Provide detailed feedback in JSON format."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500,
        temperature=0.7
    )
    
    # Get the response content
    content = response['choices'][0]['message']['content']
    
    # Try to parse and format the JSON
    try:
        # Remove any markdown code block markers if present
        content = content.replace('```json', '').replace('```', '').strip()
        # Parse the JSON
        json_data = json.loads(content)
        # Format the JSON with proper indentation
        formatted_json = json.dumps(json_data, indent=2)
        return formatted_json
    except json.JSONDecodeError:
        # If JSON parsing fails, return the original content
        return content
