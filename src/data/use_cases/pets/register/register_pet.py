from typing import Type, Dict, List
from src.data.interfaces.repositories import PetRepositoryInterface
from src.domain.use_cases import FindPetInterface
from src.domain.use_cases import RegisterPetInterface
from src.domain.models import Users, Pets


class RegisterPet(RegisterPetInterface):
    """Class to define use case: Register Pet"""

    def __init__(
        self,
        pet_repository_interface: Type[PetRepositoryInterface],
        find_user_interface: Type[FindPetInterface],
    ):
        self.pet_repository_interface = pet_repository_interface
        self.find_user_interface = find_user_interface

    def __find_user_information(
        self, user_information: Dict[int, str]
    ) -> Dict[bool, List[Users]]:
        """Check user Infos and select user
        :param - user_information: Dictionary with user_id and/or user_name
        :return - Dictionary with the response of find_use use case
        """

        user_founded = None
        user_params = user_information.keys()

        if "user_id" in user_params and "user_name" in user_params:
            user_founded = self.find_user_interface.by_id_and_name(
                user_information["user_id"], user_information["user_name"]
            )

        elif "user_id" not in user_params and "user_name" in user_params:
            user_founded = self.find_user_interface.by_name(
                user_information["user_name"]
            )

        elif "user_id" in user_params and "user_name" not in user_params:
            user_founded = self.find_user_interface.by_id(user_information["user_id"])

        else:
            return {"Success": False, "Data": None}

        return user_founded

    def registry(
        self, name: str, specie: str, user_information: Dict[int, str], age: int = None
    ) -> Dict[bool, Pets]:
        """Registry Pet
        :param - name: pet name
               - specie: type of the specie
               - age: age of the pet
               - user_information: Dictionaty with user_id and/or user_name
        :return - Dictionaty with informations of the process
        """

        response = None

        # Validating entry and trying to find an user
        validate_entry = isinstance(name, str) and isinstance(specie, str)
        user = self.__find_user_information(user_information)
        checker = validate_entry and user["Success"]

        if checker:
            response = self.pet_repository_interface.insert_pet(
                name, specie, age, user_information["user_id"]
            )

        return {"Success": checker, "Data": response}
