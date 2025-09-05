from src.scrapers.cki_scraper import CkiScraper
from src.utils.fileHandler.CkiFileHandler import CkiFileHandler

def main() -> None:
    scraper = CkiScraper()
    product_list = scraper.scrape_category("火災保險")
    CkiFileHandler.save_json(product_list)


if __name__ == "__main__":
    main()