from src.presentation.protocols import ControllerInterface
from src.infra.repositories.pet_repository import PetRepository
from src.infra.repositories.user_repository import UserRepository
from src.data.use_cases.pets.register import RegisterPet
from src.data.use_cases.users.find import FindUser
from src.presentation.controllers import RegisterPetController


def register_pet_composer() -> ControllerInterface:
    """Composing Register Pet Route
    :param - None
    :return - Object with Register Pet Route
    """

    repository = PetRepository()
    find_user_use_case = FindUser(UserRepository())
    use_case = RegisterPet(repository, find_user_use_case)
    register_pet_route = RegisterPetController(use_case)

    return register_pet_route
