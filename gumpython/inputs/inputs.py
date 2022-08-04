from abc import ABC, abstractmethod


class Input(ABC):
    @abstractmethod
    def is_valid(self):
        pass

    @abstractmethod
    def _validate(self):
        pass

    @abstractmethod
    def compile(self):
        pass
