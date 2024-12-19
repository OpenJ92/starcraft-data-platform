from abc import ABC, abstractmethod

class Injectable(ABC):
    @abstractmethod
    def process(cls, replay, session):
        """
        Process data for this ORM class.
        Must be implemented by each derived class.
        """
        pass
