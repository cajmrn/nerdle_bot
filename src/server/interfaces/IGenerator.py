from abc import ABCMeta, abstractmethod


class IGenerator(metaclass=ABCMeta):
    def __init__(self, id, mask, logger):
        self._id = id
        self._logger = logger
        self._mask = mask


    @abstractmethod
    def generate(self):
        raise NotImplementedError()
    
    # @abstractmethod
    # def log(self):
    #     raise NotImplementedError()
        