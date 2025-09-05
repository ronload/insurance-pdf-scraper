# src/model/InsuranceMetadata

from dataclasses import dataclass

@dataclass
class InsuranceMetadata:
    company_name: str
    category_name: str

    def to_dict(self) -> dict:
        return {
            "company_name": self.company_name,
            "category_name": self.category_name
        }