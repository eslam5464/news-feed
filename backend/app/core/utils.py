import random
import string
from datetime import date
from decimal import Decimal

from faker import Faker
from pydantic import (
    EmailStr,
    Field,
    AnyHttpUrl,
    field_validator,
    ConfigDict,
    BaseModel,
)


class BaseSchema(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        strict=True,
        arbitrary_types_allowed=True,
        extra="forbid",
    )


class FakerProfile(BaseSchema):
    """Base profile properties"""

    name: str
    username: str
    address: str
    birthdate: date
    blood_group: str
    company: str
    current_location: tuple[Decimal, Decimal]
    job: str
    mail: EmailStr
    residence: str
    gender: str = Field(alias="sex")
    social_security_number: str = Field(alias="ssn")
    website: list[AnyHttpUrl]
    city: str
    country: str
    flat_number: str
    street_name: str
    building_number: str
    town: str
    postal_code: str
    floor_number: str

    @field_validator("gender")
    def parse_user_gender(cls, value: str):
        if value.lower() == "f":
            return "Female"
        elif value.lower() == "m":
            return "Male"
        else:
            raise NotImplementedError("Gender value not supported")


def generate_profile() -> FakerProfile:
    faker = Faker()
    return FakerProfile(
        **faker.profile(),
        city=faker.city(),
        country=faker.country(),
        flat_number=faker.building_number(),
        street_name=faker.street_name(),
        building_number=faker.building_number(),
        town=faker.city_suffix(),
        postal_code=faker.postcode(),
        floor_number=str(faker.random_int(1, 15)),
    )


def random_string(length: int = 32) -> str:
    return "".join(random.choices(string.ascii_letters, k=length))


def random_password(length: int = 20) -> str:
    all_letters = string.ascii_letters + string.digits
    return "".join(random.choices(all_letters, k=length))


def random_long_string(no_of_sentences=7) -> str:
    faker = Faker()
    return faker.paragraph(nb_sentences=no_of_sentences)
