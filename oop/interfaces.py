from abc import abstractmethod, ABC


class LCGenerator(ABC):
    @abstractmethod
    def generate_value(self, **kwargs):
        pass


class Builder(ABC):
    @abstractmethod
    def build(self) -> list:
        pass


class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder


class OrderListStorageTemplate(ABC):
    @abstractmethod
    def create_path(self, **kwargs):
        pass

    @abstractmethod
    def write_to(self, **kwargs):
        pass

    @abstractmethod
    def read_from(self, **kwargs):
        pass

    @abstractmethod
    def connection(self):
        pass

    @abstractmethod
    def create_tale(self):
        pass
