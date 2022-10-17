from src.presentation.protocols import ControllerInterface
from src.presentation.controllers import RegisterUserController
from src.data.use_cases.users.register import RegisterUser
from src.infra.repositories.user_repository import UserRepository


def register_user_composer() -> ControllerInterface:
    """Composing Register User Route
    :param - None
    :return - Object with Register User Route
    """

    repository = UserRepository()
    use_case = RegisterUser(repository)
    register_user_route = RegisterUserController(use_case)

    return register_user_route
