import factory

from src.adapters.parts.db import models


class DbTestFactory(factory.base.Factory):
    part_id = factory.Faker("pyint")
    successful = True
    data = {}
    timestamp = factory.Faker("date_time")

    class Meta:
        model = models.Test

    @classmethod
    def create(cls, **kwargs) -> "DbTestFactory.Meta.model":
        return super().create(**kwargs)


class DbPartFactory(factory.base.Factory):
    name = "A bolt"
    modified_timestamp = factory.Faker("date_time")

    class Meta:
        model = models.Part

    @classmethod
    def create(cls, **kwargs) -> "DbPartFactory.Meta.model":
        return super().create(**kwargs)
