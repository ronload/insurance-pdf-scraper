from dataclasses import dataclass
from src.model.insurance_meta_data import InsuranceMetadata


@dataclass
class BaseInsuranceProduct:
    metadata: InsuranceMetadata
    name: str
    code: str
    term: str

    def to_dict(self) -> dict:
        return {
            "metadata": self.metadata.to_dict(),
            "name": self.name,
            "code": self.code,
            "term": self.term,
        }