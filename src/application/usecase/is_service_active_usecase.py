from dishka import FromDishka
from src.domain.repository.smartmcp_repository import SmartMCPRepository


class IsServiceActiveUsecase:
    def __init__(self, smartmcp_repository: FromDishka[SmartMCPRepository]):
        self._smartmcp_repository = smartmcp_repository

    async def execute(self) -> bool:
        return await self._smartmcp_repository.ping()
