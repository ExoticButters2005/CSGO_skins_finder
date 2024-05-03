import fastapi
import random
import uvicorn
import requests
import time

app = fastapi.FastAPI()
timer = 0


# for timer in range (0, 9999999):
#  timer = timer + 1
#  if timer % 60 == 0:
# update timer ???

# def countdown(t):
#     while t:
#         mins, secs = divmod(t, 60)
#         timer = "{:02d}:{:02d}".format(mins, secs)
#         print(timer, end="\r")
#         time.sleep(1)
#         t -= 1

#     print("update time")
# t = 60
# countdown(int(t))



def itemcheck(item_name: str):
  response = requests.request(
  method="GET",url="https://steamcommunity.com/market/search/render/?search_descriptions=0&sort_column=default&sort_dir=desc&appid=730&norender=1&count=50000",)
  content = response.json()
  item_name = content["results"]
  print(item_name)
  return item_name

itemcheck(item_name="gamma case")

# async def pricecheck(price_tag: float):
#  response = requests.request(
#    method="GET", url="https://steamcommunity.com/market/search/render/?search_descriptions=0&sort_column=default&sort_dir=desc&appid=730&norender=1&count=50000")
#  prices = response.json()
#  price_tag = (prices["sale_price_text"])
#  return price_tag

# ??????????
# "sell_price_text" = lowest listing in string
# sell_price = lowest listing in int
# market_name = item names
# market_hash_name = ???