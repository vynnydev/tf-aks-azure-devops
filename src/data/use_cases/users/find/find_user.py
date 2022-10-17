from typing import Type, Dict, List
from src.domain.use_cases import FindUserInterface
from src.data.interfaces.repositories import UserRepositoryInterface
from src.domain.models import Users as UsersModel


class FindUser(FindUserInterface):
    """Class to define use case Find User"""

    def __init__(self, user_repository_interface: Type[UserRepositoryInterface]):
        self.user_repository_interface = user_repository_interface

    def by_id(self, user_id: int) -> Dict[bool, List[UsersModel]]:
        """Select User By id
        :param - user_id: id of the user
        :param - Dictionary with informations of the process
        """

        response = None
        validate_entry = isinstance(user_id, int)

        if validate_entry:
            response = self.user_repository_interface.select_user(user_id=user_id)

        return {"Success": validate_entry, "Data": response}

    def by_name(self, name: str) -> Dict[bool, List[UsersModel]]:
        """Select User By name
        :param - name: name of the user
        :param - Dictionary with informations of the process
        """

        response = None
        validate_entry = isinstance(name, str)

        if validate_entry:
            response = self.user_repository_interface.select_user(name=name)

        return {"Success": validate_entry, "Data": response}

    def by_id_and_name(self, user_id: int, name: str) -> Dict[bool, List[UsersModel]]:
        """Select User By id and name
        :param - user_id: id of the user
                - name: name of the user
        :param - Dictionary with informations of the process
        """

        response = None
        validate_entry = isinstance(name, str) and isinstance(user_id, int)

        if validate_entry:
            response = self.user_repository_interface.select_user(
                user_id=user_id, name=name
            )

        return {"Success": validate_entry, "Data": response}
