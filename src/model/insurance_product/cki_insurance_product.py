from dataclasses import dataclass
from src.model.insurance_product.base_insurance_product import BaseInsuranceProduct

@dataclass
class CkiInsuranceProduct(BaseInsuranceProduct):
    surcharge_rate: str
    short_term_rate_and_refund_factor: str
    claims: str

    def to_dict(self) -> dict:
        return {
            "metadata": self.metadata.to_dict(),
            "name": self.name,
            "code": self.code,
            "term": self.term,
            "surcharge_rate": self.surcharge_rate,
            "short_term_rate_and_refund_factor": self.short_term_rate_and_refund_factor,
            "claims": self.claims
        }

    def __str__(self) -> str:
        return (
            f"name: {self.name}\n"
            f"code: {self.code}\n"
            f"term: {self.term}\n"
            f"surcharge_rate: {self.surcharge_rate}\n"
            f"short_term_rate_and_refund_factor: {self.short_term_rate_and_refund_factor}\n"
            f"claims: {self.claims}\n"
        )