import requests, time
from bs4 import BeautifulSoup
from .client import Client

class HttpClient(Client):

    def __init__(self, timeout: float = 10.0, duration: float = 1.0):
        super().__init__(timeout, duration)

    def get(self, url: str) -> BeautifulSoup:
        response = requests.get(url, timeout=self.timeout)
        response.raise_for_status()
        time.sleep(self.duration)

        return BeautifulSoup(response.content, "html.parser")
