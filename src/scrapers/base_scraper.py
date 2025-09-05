from abc import ABC, abstractmethod
from src.client.client import Client
from src.service.url_service.base_url_service import BaseUrlService

class BaseScraper(ABC):
    """
    給定一間保險公司的某個保險類別頁面，
    爬取該頁面上的所有保險產品資訊。
    """
    def __init__(self, client: Client, url_service: BaseUrlService):
        self.client = client
        self.url_service = url_service