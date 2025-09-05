from src.service.url_service.base_url_service import BaseUrlService

class CkiUrlService(BaseUrlService):

    category_url_map = {
        "火災保險": "https://www.cki.com.tw/page/insurance/10",
        "責任保險": "https://www.cki.com.tw/page/insurance/11",
        "工程保險": "https://www.cki.com.tw/page/insurance/12",
        "其他保險": "https://www.cki.com.tw/page/insurance/14",
        "汽車保險": "https://www.cki.com.tw/page/insurance/16",
        "旅遊保險": "https://www.cki.com.tw/page/insurance/17",
        "健康保險": "https://www.cki.com.tw/page/insurance/18",
        "傷害保險": "https://www.cki.com.tw/page/insurance/19",
        "微型保險": "https://www.cki.com.tw/page/insurance/20",
        "貨運保險": "https://www.cki.com.tw/page/insurance/21",
        "船舶保險": "https://www.cki.com.tw/page/insurance/22",
    }
    
    @classmethod
    def getCategoryUrl(cls, category_name: str) -> str:
        if category_name not in cls.category_url_map:
            raise ValueError(f"URL of category name {category_name} not found.")
        return cls.category_url_map[category_name]
    