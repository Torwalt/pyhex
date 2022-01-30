from sqlalchemy.orm.session import Session

from src.adapters.parts.db import crud
from src.domain.parts import action


def test__part_repository__crud(test_db: Session):
    pr = crud.PartRepository(test_db)
    cp = action.CreatePart(name="A bolt")
    created_p = pr.create(cp)

    assert created_p
    assert created_p.id
    assert created_p.updated_at

    p_l = pr.get_all()

    assert p_l == [created_p]

    pr.delete_by_id(created_p.id)

    p_l = pr.get_all()

    assert len(p_l) == 0


def test__part_repository__create_test(test_db: Session):
    pr = crud.PartRepository(test_db)
    cp = action.CreatePart(name="A bolt")
    created_p = pr.create(cp)

    assert created_p.id

    ct = action.CreateTest(part_id=created_p.id, successful=True, data={})
    created_t = pr.create_test(ct)

    assert created_t.timestamp.tzinfo
    assert created_t.timestamp
    assert created_t.data == ct.data
    assert created_t.part_id == created_p.id
