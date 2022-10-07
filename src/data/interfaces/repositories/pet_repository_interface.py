from abc import ABC, abstractmethod
from typing import List
from src.domain.models import Pets as PetsModel


class PetRepositoryInterface(ABC):
    """Interface to pet Repository"""

    @abstractmethod
    def insert_pet(cls, name: str, specie: str, age: int, user_id: int) -> PetsModel:
        """abstract method"""
        raise Exception("Method not implemented")

    @abstractmethod
    def select_pet(self, pet_id: int = None, user_id: int = None) -> List[PetsModel]:
        """abstractmethod"""

        raise Exception("Method not implemented")
