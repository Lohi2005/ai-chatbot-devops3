import google.genai as genai
import os

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("API key not found. Please set GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

# Use stable model
MODEL_NAME = "gemini-1.5-flash"

def get_chatbot_response(user_input: str) -> str:
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=user_input
        )
        return response.text if response.text else "No response from model."
    except Exception as e:
        return f"Error: {str(e)}"
