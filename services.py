import os
import schemas
from dotenv import load_dotenv
import requests

load_dotenv()

def gemini(content: schemas.Content):
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    response = requests.post(f'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={gemini_api_key}', json=content.model_dump())
    response_body =response.json()
    return response_body["candidates"][0]["content"]["parts"][0]["text"]

def weather(location: schemas.Location):
    weather_api_key = os.getenv("WEATHER_API_KEY")
    response = requests.post(f'http://api.weatherapi.com/v1/current.json?key={weather_api_key}&q=bulk', json=location.model_dump())
    response_body= response.json()
    return response_body["bulk"][0]