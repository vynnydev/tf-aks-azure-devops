from typing import Type
from abc import ABC, abstractmethod
from src.presentation.protocols import HttpRequest, HttpResponse


class ControllerInterface(ABC):
    """Interface to Routes"""

    @abstractmethod
    def handle(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Defining Route"""

        raise Exception("Should implement method: route")
