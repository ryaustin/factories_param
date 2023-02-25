import pytest
from datetime import datetime

from tests.factories import ProfileFactory


def test_profile_fullname(profile_factory: ProfileFactory):
    profile = profile_factory
    assert profile.full_name == f"{profile.firstname} {profile.lastname}"


def test_profile_str(profile_factory: ProfileFactory):
    profile = profile_factory
    assert (
        str(profile)
        == f"{profile.firstname} {profile.lastname} ({profile.account.username})"  # type: ignore
    )


@pytest.mark.parametrize(
    "planet, date_of_ascension, expected",
    [
        ("Earth", None, False),  # planet, date_of_ascension, expected
        ("Mars", None, True),
        ("Earth", datetime.now(), True),
        ("Mars", datetime.now(), True),
    ],
)
def test_profile_has_asscended(
    profile_factory: ProfileFactory,
    planet: str,
    date_of_ascension: datetime,
    expected: bool,
):
    profile = profile_factory
    assert not profile.is_ascended  # type: ignore


"""
To get a better understanding of how pytest.mark.parametrize works,
check out the tests below. They are equivalent to the test above.
The only difference is that they are not parametrized. 

So yay for parametrized tests! 🎉. We can reduce redundant code and
make our tests more readable.


def test_profile_has_asscended_default_state(profile_factory):
    profile = profile_factory
    assert not profile.is_ascended


def test_profile_has_asscended_with_planet(profile_factory):
    profile = profile_factory
    profile.planet = "Mars"
    assert profile.is_ascended


def test_profile_has_asscended_with_date_of_ascension(profile_factory):
    profile = profile_factory
    profile.date_of_ascension = datetime.now()
    assert profile.is_ascended


def test_profile_has_asscended_with_planet_and_date_of_ascension(profile_factory):
    profile = profile_factory
    profile.planet = "Mars"
    profile.date_of_ascension = datetime.now()
    assert profile.is_ascended
"""

# Let's write some tests to test the age property


def test_profile_age(profile_factory: ProfileFactory):
    """
    A quick note on running tests.
    You can run all tests by running `pytest` in the root directory.
    You can also run a specific test by running `pytest tests/test_accounts_and_profiles.py::test_profile_age`
    I recommend saving yourself some typing by running `pytest -k test_profile_age` instead.
    The -k flag allows you to run tests that match a specific keyword.
    """
    profile = profile_factory
    profile.date_of_birth = datetime.now()
    print(
        profile.date_of_birth
    )  # to see the output of the print statement, run `pytest -k test_profile_age -rP`
    assert profile.age == 0


"""
TODO: Try to write a parametrized test for the age property. If you get stuck, check out the solutions directory.
"""

# ----- start of your code -----
