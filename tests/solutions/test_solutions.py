# solutions.py

"""
Heres a solution to the age property test. You can run it by 
running `pytest -k test_profile_age_parametrized -rP`
"""

import pytest
from datetime import datetime, timedelta

from models.models import Profile
from tests.factories import ProfileFactory
from random import randint

r = randint(1, 100)  # totally unnecessary, but I like to use random values in my tests


@pytest.mark.parametrize(
    "date_of_birth, expected_age",
    [
        (datetime.now(), 0),
        (datetime.now() - timedelta(days=365), 1),
        (datetime.now() - timedelta(days=365 * 2), 2),
        (datetime.now() - timedelta(days=365 * 56), 56),
        (datetime.now() - timedelta(days=365 * 89), 89),
        (datetime.now() - timedelta(days=365 * r), r),  # random age
    ],
)
def test_profile_age_parametrized(
    profile_factory: ProfileFactory, date_of_birth: datetime, expected_age: int
):
    profile = profile_factory
    profile.date_of_birth = date_of_birth
    assert profile.age == expected_age
