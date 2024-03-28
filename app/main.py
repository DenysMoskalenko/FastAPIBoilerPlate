import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.examples.routes import router as examples_router
from app.core.config import get_settings
from app.lifespan import lifespan

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s %(name)s %(message)s',
)


def create_app() -> FastAPI:
    settings = get_settings()

    _app = FastAPI(title=settings.PROJECT_NAME, version='0.1.0', lifespan=lifespan)

    _app.include_router(examples_router)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )
    return _app


app = create_app()
