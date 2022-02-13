from abc import ABCMeta, abstractmethod


class IEvaluator(metaclass=ABCMeta):
    def __init__(self, solution):
        self._solution


    @abstractmethod
    def evaluate(self, guess):
        raise NotImplementedError()
        