# models.py
from datetime import datetime


class Account:
    """Represents a user account"""

    def __init__(self, username: str, email: str, date_joined: str) -> None:
        self.username = username
        self.email = email
        self.date_joined = date_joined

    def __str__(self) -> str:
        return f"{self.username} ({self.email})"

    def __repr__(self) -> str:
        return f"<Account {self.username}>"


class Profile:
    """Represents a user profile"""

    GENDER_MALE = "m"
    GENDER_FEMALE = "f"
    GENDER_UNKNOWN = "u"  # If the user refused to give it

    def __init__(
        self,
        account: Account,
        gender: str,
        firstname: str,
        lastname: str,
        date_of_birth: datetime,
        date_of_ascension=None,
        planet: str = "Earth",
    ) -> None:

        self.account = account
        self.gender = gender
        self.firstname = firstname
        self.lastname = lastname
        self.date_of_birth = date_of_birth
        self.date_of_ascension = date_of_ascension
        self.planet = planet

    def __str__(self) -> str:
        return f"{self.full_name} ({self.account.username})"

    def __repr__(self) -> str:
        return f"<Profile {self.full_name}>"

    @property
    def full_name(self) -> str:
        return f"{self.firstname} {self.lastname}"

    @property
    def age(self) -> int:
        return (datetime.today() - self.date_of_birth).days // 365

    @property
    def is_ascended(self) -> bool:
        return bool(self.date_of_ascension or self.planet != "Earth")
