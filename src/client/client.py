from abc import ABC, abstractmethod
from bs4 import BeautifulSoup

class Client(ABC):

    def __init__(self, timeout: float, duration: float) -> None:
        pass

    @abstractmethod
    def get(self, url: str) -> BeautifulSoup:
        pass