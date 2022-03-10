from abc import ABCMeta, abstractmethod
from ast import Not


class IOrchestrator(metaclass=ABCMeta):
    def __init__(self, evaluator, generator, responder, transcriber, logger):
        self._id = None
        self._logger = logger
        self._evaluator = evaluator
        self._generator = generator
        self._responder = responder
        self._transcriber = transcriber

    @abstractmethod
    def generate_id(self):
        raise NotImplementedError()

    @abstractmethod
    def evaluate(self, **generic):
        raise NotImplementedError()

    @abstractmethod
    def generate(self):
        raise NotImplementedError()
    
    @abstractmethod
    def respond(self):
        raise NotImplementedError()

    @abstractmethod
    def transcribe(self, **generic):
        raise NotImplementedError()

    @abstractmethod
    def log(self):
        raise NotImplementedError()        