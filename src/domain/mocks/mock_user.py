from faker import Faker
from src.domain.models import Users as UsersModel

faker = Faker()


def mock_users() -> UsersModel:
    """Mocking Users"""

    return UsersModel(
        id=faker.random_number(digits=5), name=faker.name(), password=faker.name()
    )
