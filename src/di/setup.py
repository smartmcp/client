from dishka import AsyncContainer, make_async_container

from .repository_provider import RepositoryProvider
from .usecase_provider import UsecaseProvider


def setup_container() -> AsyncContainer:
    return make_async_container(
        RepositoryProvider(),
        UsecaseProvider(),
    )
