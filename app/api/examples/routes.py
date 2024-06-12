from fastapi import APIRouter, Depends, Response

from app.api.examples.schemas import Example, ExampleCreate, ExampleUpdate
from app.api.examples.service import ExampleService

router = APIRouter(tags=['Examples'])


@router.post('/examples', status_code=201)
async def add_example(creation: ExampleCreate, service: ExampleService = Depends()) -> Example:
    example = await service.create_example(creation)
    return example


@router.get('/examples')
async def list_examples(service: ExampleService = Depends()) -> list[Example]:
    examples = await service.list_examples()
    return examples


@router.get('/examples/{example_id}')
async def get_example(example_id: int, service: ExampleService = Depends()) -> Example:
    example = await service.get_example_by_id(example_id)
    return example


@router.put('/examples/{example_id}')
async def change_example(example_id: int, updates: ExampleUpdate, service: ExampleService = Depends()) -> Example:
    example = await service.update_example(example_id, updates)
    return example


@router.delete('/examples/{example_id}', response_class=Response, status_code=204)
async def delete_example(example_id: int, service: ExampleService = Depends()) -> None:
    await service.delete_example_by_id(example_id)
