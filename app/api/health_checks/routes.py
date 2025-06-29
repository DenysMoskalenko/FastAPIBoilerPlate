from fastapi import APIRouter, Response

router = APIRouter(tags=['Health check'])


@router.get('/health-check', status_code=204, response_class=Response)
def health_check() -> None:
    return None
