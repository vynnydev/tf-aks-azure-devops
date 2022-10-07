from abc import ABC, abstractmethod
from typing import List
from src.domain.models import Users as UsersModel


class UserRepositoryInterface(ABC):
    """Interface to User Repository"""

    @abstractmethod
    def insert_user(self, name: str, password: str) -> UsersModel:
        """abstractmethod"""

        raise Exception("Method not implemented")

    @abstractmethod
    def select_user(self, user_id: int = None, name: str = None) -> List[UsersModel]:
        """abstractmethod"""

        raise Exception("Method not implemented")
