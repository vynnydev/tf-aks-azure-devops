from src.presentation.protocols import ControllerInterface
from src.presentation.controllers import FindUserController
from src.infra.repositories.user_repository import UserRepository
from src.data.use_cases.users.find import FindUser


def find_user_composer() -> ControllerInterface:
    """Composing Find User Route
    :param - None
    :return - Object with Find User Route
    """

    repository = UserRepository()
    use_case = FindUser(repository)
    find_user_route = FindUserController(use_case)

    return find_user_route
