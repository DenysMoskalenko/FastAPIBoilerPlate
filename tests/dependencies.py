from dataclasses import dataclass
from typing import Callable

from fastapi import FastAPI
from starlette.routing import Mount

from app.core.database import get_session


@dataclass(frozen=True, kw_only=True, slots=True)
class _DepOverride:
    dependency: Callable
    override: Callable


def override_app_test_dependencies(app: FastAPI):
    deps: list[_DepOverride] = [
        _DepOverride(dependency=get_session, override=lambda: SessionFixtureDoesNotSetExplicitly),
    ]
    for dep in deps:
        override_dependency(app, dep.dependency, dep.override)


def override_dependency(app: FastAPI, dependency: Callable, override: Callable) -> None:
    app.dependency_overrides[dependency] = override

    for route in app.router.routes:
        if isinstance(route, Mount):
            route.app.dependency_overrides[dependency] = override


class SessionFixtureDoesNotSetExplicitly: ...
