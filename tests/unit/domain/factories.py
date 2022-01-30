import factory

from src.domain.parts import part


class TestFactory(factory.base.Factory):
    id = factory.Faker("pyint")
    part_id = factory.Faker("pyint")
    successful = True
    data = {"some": "data"}
    timestamp = factory.Faker("date_time")

    class Meta:
        model = part.Test

    @classmethod
    def create(cls, **kwargs) -> "TestFactory.Meta.model":
        return super().create(**kwargs)


class PartFactory(factory.base.Factory):
    id = factory.Faker("pyint")
    name = "A bolt"
    updated_at = factory.Faker("date_time")
    tests = factory.List([])

    class Meta:
        model = part.Part

    @classmethod
    def create(cls, **kwargs) -> "PartFactory.Meta.model":
        return super().create(**kwargs)
