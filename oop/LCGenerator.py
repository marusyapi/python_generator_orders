import math


class LCGenerator:
    _multipler = math.pi
    _increment = math.e
    _modulus = 10
    _seed = 1

    @staticmethod
    def get_multipler() -> float:
        return LCGenerator._multipler

    @staticmethod
    def get_increment() -> float:
        return LCGenerator._increment

    @staticmethod
    def get_modulus() -> int:
        return LCGenerator._modulus

    @staticmethod
    def get_seed() -> int:
        return LCGenerator._seed

    @staticmethod
    def get_lcg():
        current = LCGenerator._seed
        while True:
            next_entry = (current * LCGenerator._multipler + LCGenerator._increment) % LCGenerator._modulus
            yield next_entry
            current = next_entry
