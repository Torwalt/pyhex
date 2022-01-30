from typing import List

from fastapi import APIRouter, status

from src.domain.parts import action, part, service
from src.ports.parts.http import schemas


def get_router(router: APIRouter, service: service.PartService) -> APIRouter:
    @router.get("/", response_model=List[schemas.ResponsePart])
    async def get_all_parts() -> List[schemas.ResponsePart]:
        p_l = service.get_parts()
        return [to_response_part(p) for p in p_l]

    @router.post(
        "/", response_model=schemas.ResponsePart, status_code=status.HTTP_201_CREATED
    )
    async def create_part(sp: schemas.RequestPart) -> schemas.ResponsePart:
        p = to_create_part(sp)
        n_p = service.create_part(p)
        return to_response_part(n_p)

    @router.delete("/{id}", status_code=status.HTTP_200_OK)
    async def delete_part(id: int) -> None:
        return service.delete_part(id)

    @router.post(
        "/tests",
        response_model=schemas.ResponseTest,
        status_code=status.HTTP_201_CREATED,
    )
    async def create_test(sp: schemas.RequestTest) -> schemas.ResponseTest:
        ct = to_create_test(sp)
        t = service.create_test(ct)
        return to_response_test(t)

    return router


def to_response_part(p: part.Part) -> schemas.ResponsePart:
    tests = [to_response_test(t) for t in p.tests]
    return schemas.ResponsePart(
        id=p.id, name=p.name, modified_timestamp=p.updated_at.isoformat(), tests=tests
    )


def to_response_test(t: part.Test) -> schemas.ResponseTest:
    return schemas.ResponseTest(
        id=t.id,
        part_id=t.part_id,
        successful=t.successful,
        data=t.data,
        timestamp=t.timestamp,
    )


def to_create_part(p: schemas.RequestPart) -> action.CreatePart:
    return action.CreatePart(name=p.name)


def to_create_test(t: schemas.RequestTest) -> action.CreateTest:
    return action.CreateTest(
        part_id=t.part_id, successful=t.successful, data=t.data, timestamp=t.timestamp
    )
