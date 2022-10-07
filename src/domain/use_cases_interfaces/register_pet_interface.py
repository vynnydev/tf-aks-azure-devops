from abc import ABC, abstractclassmethod
from typing import Dict
from src.domain.models import Pets as PetsModel


class RegisterPetInterface(ABC):
    """Interface to FindPet use case"""

    @abstractclassmethod
    def registry(
        cls, name: str, specie: str, user_information: Dict[int, str], age: int = None
    ) -> Dict[bool, PetsModel]:
        """use case interface"""

        raise Exception("Should implement method: registry")
