from fastapi import FastAPI
from typing import Optional
import schemas
import services

app = FastAPI()


@app.get("/")
def read_root(condition: Optional[bool] = True):
  if condition:
    return {"message": f'Hello World'}
  else:
    return {"message": f'Goodbye World'}

@app.get("/{id}")
def read_root(id: int = 5):
  return {"message": f'Hello World {id}'}


@app.post("/generate")
def generate(content: schemas.Content):
  return services.gemini(content=content)
    
@app.post("/weather")
def weather(location: schemas.Location):
  return services.weather(location=location)

@app.post("/summary")
def summary(location: schemas.Location):
  weather_details = services.weather(location=location)

  #details
  place = weather_details["query"]["location"]["name"]
  temp = weather_details["query"]["current"]["temp_c"]
  if weather_details["query"]["current"]["is_day"] == 1:
    time = "Day"
  else:
    time = "Night"
  condition = weather_details["query"]["current"]["condition"]["text"]
  wind = weather_details["query"]["current"]["wind_kph"]
  feelslike = weather_details["query"]["current"]["feelslike_c"]
  uv = weather_details["query"]["current"]["uv"]

  prompt = f'Based on this weather, please provide a concise summary, Tell me if I should carry an umbrella, Suggest appropriate clothing for going outdoors and give one or two other relevant pieces of advice (e.g., about sun protection if sunny, or driving conditions if stormy), The location is {place}, temprature in celcius is {temp} but it feels like {feelslike}, it is currently {time}time and the weather is {condition} with a uv index of {uv}, the wind speeds in kmph are {wind}.'

  gemini_request_payload = schemas.Content(
    contents=[
        schemas.Parts(
            parts=[
                schemas.Text(text = prompt)
            ]
      )
    ]
  )
  return services.gemini(content=gemini_request_payload)

