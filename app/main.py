import asyncio
import logging

from app.core.config import get_settings

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s %(name)s %(message)s',
)


async def main() -> None:
    settings = get_settings()
    print(f'{settings.PROJECT_NAME} is ready...')  # noqa: T201


if __name__ == '__main__':
    asyncio.run(main())
