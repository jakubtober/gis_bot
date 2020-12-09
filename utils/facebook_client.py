import os
import json
import facebook
import requests


class FacebookClient:
    USER_ID_FB_REQUEST_URL = r"https://graph.facebook.com/v3.0/me?access_token="

    def __init__(self):
        self.access_token = os.getenv("FB_ACCESS_TOKEN", "secret_token_string")

        user_id_response = requests.get(
            f"{self.USER_ID_FB_REQUEST_URL}{self.access_token}"
        )
        self.user_id = json.loads(user_id_response.text)

        page_response_json = json.loads(
            requests.get(
                f"https://graph.facebook.com/v3.0/{self.user_id['id']}/accounts?access_token={self.access_token}"
            ).text
        )
        self.page_id = page_response_json["data"][0]["id"]
        self.page_access_token = page_response_json["data"][0]["access_token"]

        self.graph = facebook.GraphAPI(
            access_token=self.page_access_token, version="2.12"
        )

    def get_all_posts(self):
        return self.graph.get_connections(id=self.page_id, connection_name="posts")

    def publish_post(self, title, link):
        self.graph.put_object(
            parent_object=self.page_id,
            connection_name="feed",
            message=f"""❗️❗️{title}❗️❗️""",
            link=link,
        )
