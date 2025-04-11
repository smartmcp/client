from dishka import FromDishka, Provider, Scope, provide

from src.application.usecase.is_service_active_usecase import IsServiceActiveUsecase
from src.domain.repository.smartmcp_repository import SmartMCPRepository


class UsecaseProvider(Provider):
    @provide(scope=Scope.APP)
    def is_service_active_usecase(
        self, smartmcp_repository: FromDishka[SmartMCPRepository]
    ) -> IsServiceActiveUsecase:
        return IsServiceActiveUsecase(smartmcp_repository=smartmcp_repository)
