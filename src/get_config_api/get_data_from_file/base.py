"""Base class for file handler"""

from abc import ABC, abstractmethod


class FileHandler(ABC):
    """Abstract class for file handler"""

    @abstractmethod
    def read_file(self, file_path: str):
        """Return the contents of the file"""
        pass