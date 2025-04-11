from dishka import Provider, provide, Scope

from src.domain.repository.smartmcp_repository import SmartMCPRepository
from src.infrastructure.repository.smartmcp_repository_impl import (
    SmartMCPRepositoryImpl,
)


class RepositoryProvider(Provider):
    @provide(scope=Scope.APP)
    def smartmcp_repository(self) -> SmartMCPRepository:
        return SmartMCPRepositoryImpl()
