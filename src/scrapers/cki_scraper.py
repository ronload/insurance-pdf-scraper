import re
from bs4 import BeautifulSoup
from bs4.element import PageElement, Tag
from urllib.parse import urljoin
from typing import Sequence
from src.scrapers.base_scraper import BaseScraper
from src.client.http_client import HttpClient
from src.service.url_service.cki_url_service import CkiUrlService
from src.utils.parsers.cki_parser import CkiParser
from src.model.insurance_product.cki_insurance_product import CkiInsuranceProduct

class CkiScraper(BaseScraper):

    BASE_URL = "https://www.cki.com.tw"
    def __init__(self):
        super().__init__(
            client=HttpClient(timeout=10.0, duration=0.0), 
            url_service=CkiUrlService()
        )

    def _extract_urls_from_ul(self, ul: Tag) -> list[str]:
        li_seq = ul.find_all('li')
        result = []
        for li in li_seq:
            if not isinstance(li, Tag):
                continue
            onclick = li.get('onclick')
            if not isinstance(onclick, str):
                continue
            match = re.search(r"window\.open\('(.+?)'\)", onclick)
            if not match:
                continue 
            relative_path = match.group(1)
            full_url = urljoin(self.BASE_URL, relative_path)
            result.append(full_url)

        return result

    def get_insurance_url_list(self, category_name: str) -> list[str]:
        """取得一個分類頁面中的所有產品連結。"""
        try:
            # 取得分類頁面連結
            category_url = self.url_service.getCategoryUrl(category_name)
            """
            取得列表元素
            頁面中會存在多個名為 document-list 的 ul element
            這些 ul element 中存在的 li 就有我們要的產品連結
            """
            print(f"Scraping page:{category_url}")
            content: BeautifulSoup = self.client.get(category_url)
            document_lists: Sequence[PageElement] = content.find_all('ul', class_='document-list')
            result: list[str] = []

            for ul in document_lists:
                if not isinstance(ul, Tag):
                    continue
                result += self._extract_urls_from_ul(ul)
                
            return result
        except Exception as e:
            print(f"An error occurred: {e}")
            return []
        
    def scrape_category(self, category_name: str):
        insurance_url_list = self.get_insurance_url_list(category_name)
        insurance_product_list: list[CkiInsuranceProduct] = []

        try:
            for url in insurance_url_list:
                content = self.client.get(url)
                table = content.find('table')
                if not isinstance(table, Tag):
                    continue
                product_instance = CkiParser.parse_product_info(table, category_name)
                print(product_instance)
                insurance_product_list.append(product_instance)
        except KeyboardInterrupt:
            print("Interrupted by user")
        except Exception as e:
            print(f"An error occurred: {e}")
        
        return insurance_product_list