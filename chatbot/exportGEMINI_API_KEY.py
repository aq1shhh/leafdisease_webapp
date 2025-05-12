import google.generativeai as genai

genai.configure(api_key="AIzaSyAcUbQWkQGAybEICXai9Vw-hUkzv7PB04Q")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Explain how AI works")
print(response.text)