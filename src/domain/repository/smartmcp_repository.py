from abc import ABC, abstractmethod


class SmartMCPRepository(ABC):
    @abstractmethod
    async def ping(self) -> bool:
        """Returns True if the server is online."""
