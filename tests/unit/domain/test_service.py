from unittest import mock

import pytest

from src.domain.parts import repository
from src.domain.parts.service import PartService
from tests.unit.domain import factories


@pytest.fixture
def part_service():
    p_rep = mock.MagicMock(repository.PartRepository)
    return PartService(p_rep)


def test__get_parts(part_service: PartService):
    exp_p = [factories.PartFactory.create()]
    part_service.repo.get_all.return_value = exp_p

    actual_parts = part_service.get_parts()

    assert exp_p == actual_parts


def test__create_part(part_service: PartService):
    part = factories.PartFactory.create()
    part_service.repo.create.return_value = part

    actual_parts = part_service.create_part(part)

    assert part == actual_parts


def test__delete_part(part_service: PartService):
    part = factories.PartFactory.create()
    part_service.delete_part(part.id)

    assert part_service.repo.delete_by_id.call_count == 1
