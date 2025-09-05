from abc import ABC, abstractmethod

class BaseUrlService(ABC):

    @classmethod
    @abstractmethod
    def getCategoryUrl(cls, category_name: str) -> str:
        pass