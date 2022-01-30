import factory

from src.ports.parts.http import schemas


class HttpPartFactory(factory.base.Factory):
    id = factory.Faker("pyint")
    name = "A bolt"
    modified_timestamp = factory.Faker("date_time")

    class Meta:
        model = schemas.ResponsePart

    @classmethod
    def create(cls, **kwargs) -> "HttpPartFactory.Meta.model":
        return super().create(**kwargs)
