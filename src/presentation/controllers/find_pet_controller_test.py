from faker import Faker
from src.data.use_cases.pets.find.test import FindPetSpy
from src.infra.repositories.spies import PetRepositorySpy
from src.presentation.protocols import HttpRequest
from .find_pet_controller import FindPetController

faker = Faker()


def test_handle():
    """Testing controller method in FindPetController"""

    find_pet_use_case = FindPetSpy(PetRepositorySpy())
    find_pet_controller = FindPetController(find_pet_use_case)
    attributes = {
        "pet_id": faker.random_number(digits=2),
        "user_id": faker.random_number(digits=2),
    }

    http_request = HttpRequest(query=attributes)

    http_response = find_pet_controller.handle(http_request)

    # Testing input
    assert (
        find_pet_use_case.by_pet_id_and_user_id_param["pet_id"] == attributes["pet_id"]
    )
    assert (
        find_pet_use_case.by_pet_id_and_user_id_param["user_id"]
        == attributes["user_id"]
    )

    # Testing output
    assert http_response.status_code == 200
    assert "error" not in http_response.body


def test_handle_by_pet_id():
    """Testing handle method in FindPetController"""

    find_pet_use_case = FindPetSpy(PetRepositorySpy())
    find_pet_controller = FindPetController(find_pet_use_case)
    attributes = {"pet_id": faker.random_number(digits=2)}

    http_request = HttpRequest(query=attributes)

    http_response = find_pet_controller.handle(http_request)

    # Testing input
    assert find_pet_use_case.by_pet_id_param["pet_id"] == attributes["pet_id"]

    # Testing output
    assert http_response.status_code == 200
    assert "error" not in http_response.body


def test_handle_by_user_id():
    """Testing handle method in FindPetController"""

    find_pet_use_case = FindPetSpy(PetRepositorySpy())
    find_pet_controller = FindPetController(find_pet_use_case)
    attributes = {"user_id": faker.random_number(digits=2)}

    http_request = HttpRequest(query=attributes)

    http_response = find_pet_controller.handle(http_request)

    # Testing input
    assert find_pet_use_case.by_user_id_param["user_id"] == attributes["user_id"]

    # Testing output
    assert http_response.status_code == 200
    assert "error" not in http_response.body


def test_handle_error_no_query():
    """Testing handle method in FindPetController"""

    find_pet_use_case = FindPetSpy(PetRepositorySpy())
    find_pet_controller = FindPetController(find_pet_use_case)

    http_request = HttpRequest()

    http_response = find_pet_controller.handle(http_request)

    # Testing input
    assert find_pet_use_case.by_pet_id_param == {}
    assert find_pet_use_case.by_user_id_param == {}
    assert find_pet_use_case.by_pet_id_and_user_id_param == {}

    # Testing output
    assert http_response.status_code == 400
    assert "error" in http_response.body


def test_handle_error_wrong_query():
    """Testing handle method in FindPetController"""

    find_pet_use_case = FindPetSpy(PetRepositorySpy())
    find_pet_controller = FindPetController(find_pet_use_case)

    http_request = HttpRequest(query={"something": faker.random_number(digits=2)})

    http_response = find_pet_controller.handle(http_request)

    # Testing input
    assert find_pet_use_case.by_pet_id_param == {}
    assert find_pet_use_case.by_user_id_param == {}
    assert find_pet_use_case.by_pet_id_and_user_id_param == {}

    # Testing output
    assert http_response.status_code == 422
    assert "error" in http_response.body
