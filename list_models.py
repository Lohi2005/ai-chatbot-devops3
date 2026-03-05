import google.genai as genai

client = genai.Client(api_key="AIzaSyYourGoogleKeyHere")

print("Available models:")
for m in client.models.list():
    print(m.name)
