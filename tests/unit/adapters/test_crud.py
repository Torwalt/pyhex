from unittest import mock

import pytest
from sqlalchemy.orm import Session

from src.adapters.parts.db import crud
from src.domain.parts import part
from tests.unit.adapters import factories


@pytest.fixture
def part_repository():
    m_sess = mock.MagicMock(Session)
    return crud.PartRepository(m_sess)


def test_part_repository__get_all(part_repository: crud.PartRepository):
    expected_dbp = [factories.DbPartFactory.create()]
    expected_return = [crud.to_part(expected_dbp[0], [])]

    m_execute = mock.MagicMock()
    m_scalars = mock.MagicMock()
    part_repository.db.execute.return_value = m_execute
    m_execute.scalars.return_value = m_scalars
    m_scalars.all.return_value = expected_dbp

    p_l = part_repository.get_all()

    assert expected_return == p_l


def test_to_part():
    db_p = factories.DbPartFactory.create()
    p = crud.to_part(db_p, [])
    expected_part = part.Part(
        id=db_p.id, name=db_p.name, updated_at=db_p.modified_timestamp, tests=[]
    )
    assert p == expected_part
