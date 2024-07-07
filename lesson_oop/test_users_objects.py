import csv
import pytest

from lesson_oop.models.providers import UserProvider, CsvUserProvider, DatabaseUserProvider, ApiUserProvider
from lesson_oop.models.users import User, USER_ADULT_AGE, Status


@pytest.fixture(params=[CsvUserProvider, DatabaseUserProvider, ApiUserProvider])
def user_provider(request) -> UserProvider:
    return request.param()

@pytest.fixture
def users(user_provider) -> list[User]:
    return user_provider.get_users()


@pytest.fixture
def workers(users) -> list[User]:
    workers = [user for user in users if user.status == Status.worker]
    return workers


# def test_workers_are_adults_v2(workers):
#     for worker in workers:
#         assert user_is_adult(worker), f"Worker {worker['name']} младше 18 лет"


def test_workers_are_adults_v3(workers):
    for worker in workers:
        assert worker.is_adult(), f"Worker {worker.name} младше {USER_ADULT_AGE} лет"
