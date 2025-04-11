import asyncio

from src.infrastructure.log.setup import setup_logger
from src.di.setup import setup_container
from src.presentation.setup import setup_bot


async def main() -> None:
    setup_logger()

    container = setup_container()

    await setup_bot(container=container)


if __name__ == "__main__":
    asyncio.run(main())
