import json
import requests

graeph_api_version = "v3.0"
app_id = ""
app_secret = ""
your_user_access_token = ""

url = f"""https://graph.facebook.com/{graeph_api_version}/oauth/access_token?grant_type=fb_exchange_token&client_id={app_id}&client_secret={app_secret}&fb_exchange_token={your_user_access_token}"""

page_response_json = json.loads(requests.get(url).text)

print(page_response_json)
