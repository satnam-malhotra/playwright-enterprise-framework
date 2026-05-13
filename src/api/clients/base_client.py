import requests
class BaseClient:
    def __init__(self):
        self.session = requests.Session()
        self.base_url = "https://reqres.in/api"

    def get(self, url, params=None):
        return self.session.get(f"{self.base_url}/{url}", params=params)

    def post(self, url, payload=None):
        return self.session.post(f"{self.base_url}/{url}", json=payload)