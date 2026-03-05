import google.genai as genai

# Replace with a valid Gemini API key from Google AI Studio
client = genai.Client(api_key="AIzaSyAHGOFIXVwOLNvyVXSaY407VzJFN9ULRH0")

# Automatically pick the first available model
def get_chatbot_response(user_input: str) -> str:
    # List models once and pick the first
    models = list(client.models.list())
    if not models:
        return "No models available for this API key."
    
    model_name = models[0].name  # e.g., "models/gemini-pro"
    
    response = client.models.generate_content(
        model=model_name,
        contents=user_input
    )
    return response.text
