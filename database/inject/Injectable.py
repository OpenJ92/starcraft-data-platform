from abc import ABC, abstractmethod

class Injectable(ABC):
    @classmethod
    @property
    @abstractmethod
    def __tableschema__(cls):
        """Return the schema name. Must be implemented by subclasses."""
        pass

    @classmethod
    @abstractmethod
    def process(cls, replay, session):
        """Must be implemented by subclasses."""
        pass
