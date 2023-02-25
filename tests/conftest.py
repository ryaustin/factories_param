import pytest

from pytest_factoryboy import register

from .factories import AccountFactory, ProfileFactory

register(AccountFactory)  # => account_factory
register(ProfileFactory)  # => profile_factory


@pytest.fixture
def profile_factory():
    return ProfileFactory()
