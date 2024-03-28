from polyfactory.factories.pydantic_factory import ModelFactory

from app.api.examples.schemas import ExampleCreate


class ExampleCreationFactory(ModelFactory[ExampleCreate]):
    __model__ = ExampleCreate
