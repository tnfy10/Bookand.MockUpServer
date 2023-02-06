from http import HTTPStatus

from faker import Faker
from faker.providers import DynamicProvider

image_url_provider = DynamicProvider(
    provider_name="image_url",
    elements=["https://http.cat/" + str(status_code) for status_code in list(HTTPStatus)]
)

fake = Faker("ko_KR")

fake.add_provider(image_url_provider)
