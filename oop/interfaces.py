from abc import abstractmethod, ABC


class ILCGenerator(ABC):
    @abstractmethod
    def generate_value(self):
        pass


class IOrderBuilder(ABC):
    @abstractmethod
    def build(self) -> list:
        pass
