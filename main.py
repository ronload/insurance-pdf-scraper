from src.scrapers.cki_scraper import CkiScraper
from src.utils.fileHandler.CkiFileHandler import CkiFileHandler
from src.service.url_service.cki_url_service import CkiUrlService

def main() -> None:
    scraper = CkiScraper()
    for category in CkiUrlService.category_url_map.keys():
        product_list = scraper.scrape_category(category)
        CkiFileHandler.save_json(product_list)

if __name__ == "__main__":
    main()