from typing import Type, Dict
from src.domain.use_cases_interfaces import RegisterUserInterface
from src.data.interfaces.repositories import UserRepositoryInterface
from src.domain.models import Users as UsersModel


class RegisterUser(RegisterUserInterface):
    """Class to define user case for register user"""

    def __init__(self, user_repository: Type[UserRepositoryInterface]):
        self.user_repository = user_repository

    def register(self, name: str, password: str) -> Dict[bool, UsersModel]:
        """Register user case
        :param - name: person name
        - password: password of the person
        :return - dictionary with information of the process
        """

        response = None
        validate_entry = isinstance(name, str) and isinstance(password, str)

        if validate_entry:
            response = self.user_repository.insert_user(name, password)

        return {"Success": validate_entry, "Data": response}
