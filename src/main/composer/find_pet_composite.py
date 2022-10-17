from src.presentation.protocols import ControllerInterface
from src.presentation.controllers import FindPetController
from src.infra.repositories.pet_repository import PetRepository
from src.data.use_cases.pets.find import FindPet


def find_pet_composer() -> ControllerInterface:
    """Composing Find Pet Route
    :param - None
    :return - Object with Find Pet Route
    """

    repository = PetRepository()
    use_case = FindPet(repository)
    find_pet_route = FindPetController(use_case)

    return find_pet_route
