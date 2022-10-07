from faker import Faker
from src.domain.models import Pets as PetsModel

faker = Faker()


def mock_pet() -> PetsModel:
    """Mocking Pet
    :param - None
    :return - Fake Pet registry
    """

    return PetsModel(
        id=faker.random_number(digits=5),
        name=faker.name(),
        specie="dog",
        age=faker.random_number(digits=1),
        user_id=faker.random_number(digits=5),
    )
