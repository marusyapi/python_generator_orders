from abc import abstractmethod, ABC


class ILCGenerator(ABC):
    @abstractmethod
    def generate_value(self):
        pass


class IOrderBuilder(ABC):
    @abstractmethod
    def build(self,
              id,
              instrument,
              px_init,
              px_fill,
              volume_init,
              volume_fill,
              side,
              status,
              date,
              note,
              tag) -> list:
        pass


class IOrderListStorageTemplate(ABC):
    @abstractmethod
    def create_path(self, a):
        pass

    @abstractmethod
    def write_to(self, a, b, c):
        pass

    @abstractmethod
    def read_from(self, a):
        pass
