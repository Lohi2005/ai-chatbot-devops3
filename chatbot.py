import google.genai as genai

# Your Gemini API key
client = genai.Client(api_key="YOUR_API_KEY")

def get_chatbot_response(user_input: str) -> str:
    models = list(client.models.list())

    if not models:
        return "No models available."

    model_name = models[0].name

    response = client.models.generate_content(
        model=model_name,
        contents=user_input
    )

    return response.text
