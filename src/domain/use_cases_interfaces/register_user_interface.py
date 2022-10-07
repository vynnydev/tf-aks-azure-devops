from typing import Dict
from abc import ABC, abstractclassmethod
from src.domain.models import Users as UsersModel


class RegisterUserInterface(ABC):
    """Interface to RegisterUser use case"""

    @abstractclassmethod
    def register(cls, name: str, password: str) -> Dict[bool, UsersModel]:
        """use case interface"""

        raise Exception("Should implement method: register")
