from datetime import datetime

from pydantic import BaseModel


class RequestTest(BaseModel):
    part_id: int
    successful: bool
    data: dict
    timestamp: datetime


class ResponseTest(BaseModel):
    id: int
    part_id: int
    successful: bool
    data: dict
    timestamp: datetime


class ResponsePart(BaseModel):
    id: int
    name: str
    modified_timestamp: datetime
    tests: list[ResponseTest]


class RequestPart(BaseModel):
    name: str
