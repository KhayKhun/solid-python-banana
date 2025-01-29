import requests
import dotenv
import os

dotenv.load_dotenv()
token = os.environ['TOKEN']
url = os.environ['AIRQ_API_URL']

request_url = url.replace("#city#", "Bangkok")
request_url = request_url.replace("#token#", token)

print(request_url)

response = requests.get(request_url)
json_data = response.json()["data"]


print(json_data['city'], json_data['aqi'])