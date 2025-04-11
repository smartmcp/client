import asyncio

from src.infrastructure.log.setup import setup_logger
from src.di.setup import setup_container


async def main() -> None:
    setup_logger()

    setup_container()


if __name__ == "__main__":
    asyncio.run(main())
