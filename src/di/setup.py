from dishka import Container, make_container

from .repository_provider import RepositoryProvider


def setup_container() -> Container:
    return make_container(RepositoryProvider())
