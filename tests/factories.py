from datetime import datetime
import factory
import random
from faker import Faker

from models.models import Account, Profile

fake = Faker()


class AccountFactory(factory.Factory):
    class Meta:
        model = Account

    _account = fake.simple_profile()

    username = _account.get("username")
    email = _account.get("mail")
    date_joined = factory.LazyFunction(datetime.now)


class ProfileFactory(factory.Factory):
    class Meta:
        model = Profile

    account = factory.SubFactory(AccountFactory)
    _account = account.get_factory()._account  # type: ignore
    gender = _account.get("sex")
    firstname = _account.get("name").split(" ")[0]
    lastname = _account.get("name").split(" ")[1]
    date_of_birth = datetime.combine(
        _account.get("birthdate"), datetime.min.time()
    )  # convert date to datetime
