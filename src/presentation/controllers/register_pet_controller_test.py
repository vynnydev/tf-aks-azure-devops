from faker import Faker
from src.data.use_cases.pets.register.test import RegisterPetSpy
from src.presentation.protocols import HttpRequest
from src.infra.repositories.spies import PetRepositorySpy, UserRepositorySpy
from .register_pet_controller import RegisterPetController

faker = Faker()


def test_controller():
    """Testing controller method in RegisterUserController"""

    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), UserRepositorySpy())
    register_pet_controller = RegisterPetController(register_pet_use_case)
    attributes = {
        "name": faker.word(),
        "specie": "Dog",
        "age": faker.random_number(),
        "user_information": {
            "user_id": faker.random_number(),
            "user_name": faker.word(),
        },
    }

    response = register_pet_controller.handle(HttpRequest(body=attributes))

    # Testing input
    assert register_pet_use_case.registry_param["name"] == attributes["name"]
    assert register_pet_use_case.registry_param["specie"] == attributes["specie"]
    assert register_pet_use_case.registry_param["age"] == attributes["age"]
    assert (
        register_pet_use_case.registry_param["user_information"]
        == attributes["user_information"]
    )

    # Testing output
    assert response.status_code == 200
    assert "error" not in response.body


def test_controller_without_age():
    """Testing controller method in RegisterUserController"""

    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), UserRepositorySpy())
    register_pet_controller = RegisterPetController(register_pet_use_case)
    attributes = {
        "name": faker.word(),
        "specie": "Dog",
        "user_information": {
            "user_id": faker.random_number(),
            "user_name": faker.word(),
        },
    }

    response = register_pet_controller.handle(HttpRequest(body=attributes))

    # Testing input
    assert register_pet_use_case.registry_param["name"] == attributes["name"]
    assert register_pet_use_case.registry_param["specie"] == attributes["specie"]
    assert register_pet_use_case.registry_param["age"] is None
    assert (
        register_pet_use_case.registry_param["user_information"]
        == attributes["user_information"]
    )

    # Testing output
    assert response.status_code == 200
    assert "error" not in response.body


def test_controller_user_id_in_user_information():
    """Testing controller method in RegisterUserController"""

    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), UserRepositorySpy())
    register_pet_controller = RegisterPetController(register_pet_use_case)

    attributes = {
        "name": faker.word(),
        "specie": "Dog",
        "user_information": {"user_name": faker.word()},
    }

    response = register_pet_controller.handle(HttpRequest(body=attributes))

    # Testing input
    assert register_pet_use_case.registry_param["name"] == attributes["name"]
    assert register_pet_use_case.registry_param["specie"] == attributes["specie"]
    assert register_pet_use_case.registry_param["age"] is None
    assert (
        register_pet_use_case.registry_param["user_information"]
        == attributes["user_information"]
    )

    # Testing output
    assert response.status_code == 200
    assert "error" not in response.body


def test_controller_error_no_body():
    """Testing controller method in RegisterUserController"""

    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), UserRepositorySpy())
    register_pet_controller = RegisterPetController(register_pet_use_case)

    response = register_pet_controller.handle(HttpRequest())

    # Testing input
    assert register_pet_use_case.registry_param == {}

    # Testing output
    assert response.status_code == 400
    assert "error" in response.body


def test_controller_error_wrong_body():
    """Testing controller method in RegisterUserController"""

    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), UserRepositorySpy())
    register_pet_controller = RegisterPetController(register_pet_use_case)

    attributes = {
        "specie": "Dog",
        "user_information": {
            "user_id": faker.random_number(),
            "user_name": faker.word(),
        },
    }

    response = register_pet_controller.handle(HttpRequest(body=attributes))

    # Testing input
    assert register_pet_use_case.registry_param == {}

    # Testing output
    assert response.status_code == 422
    assert "error" in response.body


def test_controller_error_wrong_user_information():
    """Testing controller method in RegisterUserController"""

    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), UserRepositorySpy())
    register_pet_controller = RegisterPetController(register_pet_use_case)

    attributes = {"name": faker.word(), "specie": "Dog", "user_information": {}}

    response = register_pet_controller.handle(HttpRequest(body=attributes))

    # Testing input
    assert register_pet_use_case.registry_param == {}

    # Testing output
    assert response.status_code == 422
    assert "error" in response.body
