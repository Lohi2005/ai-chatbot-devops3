import google.genai as genai
import os

# Use API key from environment (IMPORTANT for Docker/Jenkins)
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# FIXED model (do NOT dynamically fetch)
MODEL_NAME = "gemini-1.5-flash"

def get_chatbot_response(user_input: str) -> str:
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=user_input
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
