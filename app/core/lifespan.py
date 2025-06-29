from contextlib import asynccontextmanager
from typing import Any, AsyncGenerator

from fastapi import FastAPI

from app.core.config import get_settings, Settings


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, Any]:
    settings = get_settings()
    await startup(settings)
    yield
    await shutdown()


async def startup(settings: Settings) -> None: ...


async def shutdown() -> None: ...
