from src.domain.repository.smartmcp_repository import SmartMCPRepository


class SmartMCPRepositoryImpl(SmartMCPRepository):
    async def ping(self) -> bool:
        return False
