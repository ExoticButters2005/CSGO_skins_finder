import fastapi
import random
import uvicorn
import requests
import time

app = fastapi.FastAPI()
timer = 0

def itemcheck(item_name: str):
  response = requests.request(
  method="GET",url="https://steamcommunity.com/market/search/render/?search_descriptions=0&sort_column=default&sort_dir=desc&appid=730&norender=1&count=50000",)
  content = response.json()
  item_name = content["results"]
  print(item_name)
  return item_name

itemcheck(item_name="gamma case")

