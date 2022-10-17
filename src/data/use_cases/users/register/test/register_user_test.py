from faker import Faker
from src.infra.repositories.spies import UserRepositorySpy
from ..register_user import RegisterUser

faker = Faker()


def test_register():
    """Testing registry method"""

    user_repo = UserRepositorySpy()
    register_user = RegisterUser(user_repo)

    attributes = {"name": faker.name(), "password": faker.name()}

    response = register_user.register(
        name=attributes["name"], password=attributes["password"]
    )

    # Testing inputs
    assert user_repo.insert_user_params["name"] == attributes["name"]
    assert user_repo.insert_user_params["password"] == attributes["password"]

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]
