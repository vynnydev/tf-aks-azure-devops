from faker import Faker
from src.data.use_cases.users.register.test import RegisterUserSpy
from src.presentation.protocols import HttpRequest
from src.infra.repositories.spies import UserRepositorySpy
from .register_user_controller import RegisterUserController

faker = Faker()


def test_controller():
    """Testing controller method in RegisterUserController"""

    register_user_use_case = RegisterUserSpy(UserRepositorySpy())
    register_user_controller = RegisterUserController(register_user_use_case)
    attributes = {"name": faker.word(), "password": faker.word()}

    response = register_user_controller.handle(HttpRequest(body=attributes))

    # Testing input
    assert register_user_use_case.register_param["name"] == attributes["name"]
    assert register_user_use_case.register_param["password"] == attributes["password"]

    # Testing output
    assert response.status_code == 200
    assert "error" not in response.body


def test_controller_error_no_body():
    """Testing controller method in RegisterUserController"""

    register_user_use_case = RegisterUserSpy(UserRepositorySpy())
    register_user_controller = RegisterUserController(register_user_use_case)

    response = register_user_controller.handle(HttpRequest())

    # Testing input
    assert register_user_use_case.register_param == {}

    # Testing output
    assert response.status_code == 400
    assert "error" in response.body


def test_controller_error_wrong_body():
    """Testing controller method in RegisterUserController"""

    register_user_use_case = RegisterUserSpy(UserRepositorySpy())
    register_user_controller = RegisterUserController(register_user_use_case)
    attributes = {"name": faker.word()}

    response = register_user_controller.handle(HttpRequest(body=attributes))

    # Testing input
    assert register_user_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert "error" in response.body
