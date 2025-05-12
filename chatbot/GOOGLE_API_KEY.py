import google.generativeai as genai

genai.configure(api_key="AIzaSyAcUbQWkQGAybEICXai9Vw-hUkzv7PB04Q")

models = genai.list_models()
for model in models:
    print(model.name)
