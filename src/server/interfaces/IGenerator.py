from abc import ABCMeta, abstractmethod


class IGenerator(metaclass=ABCMeta):
    def __init__(self, mask):
        self._mask = mask


    @abstractmethod
    def generate(self):
        raise NotImplementedError()
        