from asyncio import DefaultEventLoopPolicy
from typing import Any, AsyncGenerator

from fastapi import FastAPI
from httpx import ASGITransport, AsyncClient
import pytest

from tests.dependencies import override_app_test_dependencies

TEST_HOST = 'http://test'


def pytest_configure(config: pytest.Config) -> None:
    """
    Allows plugins and conftest files to perform initial configuration.
    This hook is called for every plugin and initial conftest
    file after command line options have been parsed.
    """


@pytest.fixture(scope='session')
async def app() -> AsyncGenerator[FastAPI, Any]:
    from app.main import create_app

    _app = create_app()
    override_app_test_dependencies(_app)

    yield _app


@pytest.fixture(scope='session')
async def client(app: FastAPI) -> AsyncGenerator[AsyncClient, Any]:
    async with AsyncClient(transport=ASGITransport(app=app), base_url=TEST_HOST) as client:
        yield client


@pytest.fixture(scope='session', params=(DefaultEventLoopPolicy(),))
def event_loop_policy(request):
    return request.param
