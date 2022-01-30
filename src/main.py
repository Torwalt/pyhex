import fastapi

from src.adapters.parts.db import crud, database
from src.config import Settings
from src.domain.parts import service
from src.ports.parts.http import endpoints as part_endpoints


def create_app(service: service.PartService) -> fastapi.FastAPI:
    """
    Build the server object and configure the routes.
    """
    app = fastapi.FastAPI(
        title="pyhex", openapi_url="/api/openapi.json", version="0.1.0"
    )

    api_router = fastapi.APIRouter()
    part_router = fastapi.APIRouter()
    api_router.include_router(
        part_endpoints.get_router(part_router, service), prefix="/parts"
    )

    app.include_router(api_router, prefix="/api")
    return app


def build_part_service(s: Settings) -> service.PartService:
    """
    Create the parts service.
    """
    db = database.create_db(s)
    parts_repo = crud.PartRepository(db)
    return service.PartService(parts_repo)


settings = Settings()
ps = build_part_service(settings)
app = create_app(ps)
