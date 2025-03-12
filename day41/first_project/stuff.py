import requests

# res = requests.get("https://wcoding.com")
# print("RES:", res.text)
# print(dir(res))

res = requests.get("https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita")
# print("RES:", res.text)
# print("RES:", res.json())
resObj = res.json()
print("RES:", ", ".join([drink["strDrink"] for drink in resObj["drinks"]]))

