import json
import os
from src.model.insurance_product.cki_insurance_product import CkiInsuranceProduct

class CkiFileHandler:

    @classmethod
    def save_json(cls, product_list: list[CkiInsuranceProduct]) -> None:
        # 按公司和類別分組
        grouped_products = {}
        
        for product in product_list:
            company_name = product.metadata.company_name
            category_name = product.metadata.category_name
            
            key = (company_name, category_name)
            if key not in grouped_products:
                grouped_products[key] = []
            grouped_products[key].append(product)
        
        # 為每個分組創建一個JSON檔案
        for (company_name, category_name), products in grouped_products.items():
            # 創建目錄路徑
            dir_path = os.path.join("data", "raw", company_name, category_name)
            os.makedirs(dir_path, exist_ok=True)
            
            # 創建檔案路徑
            file_path = os.path.join(dir_path, f"{category_name}_products.json")
            
            try:
                # 將所有產品轉換為字典列表
                products_data = [product.to_dict() for product in products]
                
                # 保存為JSON檔案
                with open(file_path, "w", encoding="utf-8") as f:
                    json.dump(products_data, f, ensure_ascii=False, indent=4)
                
                print(f"Saved {len(products)} products to {file_path}")
                
            except Exception as e:
                print(f"An error occurred while saving {file_path}: {e}")
                continue
            