from urllib.parse import urljoin
from bs4.element import Tag
from src.model.insurance_meta_data import InsuranceMetadata
from src.model.insurance_product.cki_insurance_product import CkiInsuranceProduct

class CkiParser:

    BASE_URL = "https://www.cki.com.tw"
    @classmethod
    def _get_name_by_parse_title(cls, table: Tag) -> str:
        thread = table.find('thead')
        if not isinstance(thread, Tag):
            return ""
        tr = thread.find('tr')
        if not isinstance(tr, Tag):
            return ""
        th = tr.find('th')
        if not isinstance(th, Tag):
            return ""
        name_tag = th.find_next('th')
        if not isinstance(name_tag, Tag):
            return ""
        return name_tag.text.strip().replace('\n', '')

    @classmethod
    def _get_attrs(cls, table: Tag) -> list[str]:
        tbody = table.find('tbody')
        if not isinstance(tbody, Tag):
            return []
        attrs = []
        rows = tbody.find_all('tr')
        for row in rows:
            if not isinstance(row, Tag):
                continue
            cells = row.find_all('td')
            if len(cells) < 2:
                continue
            value_cell = cells[1]
            links = value_cell.find_all('a')  #type: ignore

            if links:
                pdf_url = links[0].get('href', '')  #type: ignore
                pdf_url = urljoin(cls.BASE_URL, pdf_url)   #type: ignore
                attrs.append(pdf_url)
            else:
                attrs.append(value_cell.get_text(strip=True).replace('\n', ', '))
        return attrs

    @classmethod
    def parse_product_info(cls, table: Tag, category_name: str) -> CkiInsuranceProduct:
        attrs = cls._get_attrs(table)
        return CkiInsuranceProduct(
            metadata = InsuranceMetadata(
                company_name = "CKI",
                category_name = category_name
            ),
            name = cls._get_name_by_parse_title(table),
            code = attrs[0],
            term = attrs[1],
            surcharge_rate = attrs[2],
            short_term_rate_and_refund_factor = attrs[3],
            claims = attrs[4]
        )