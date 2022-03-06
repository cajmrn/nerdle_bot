from abc import ABCMeta, abstractmethod
from ast import Not


class IOrchestrator(metaclass=ABCMeta):
    def __init__(self, evaluator, generator, responder, logger):
        self._logger = logger
        self._evaluator = evaluator
        self._generator = generator
        self._responder = responder

    @abstractmethod
    def evaluate(self):
        raise NotImplementedError()

    @abstractmethod
    def generate(self):
        raise NotImplementedError()
    
    @abstractmethod
    def respond(self):
        raise NotImplementedError()

    @abstractmethod
    def log(self):
        raise NotImplementedError()        