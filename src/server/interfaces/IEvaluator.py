from abc import ABCMeta, abstractmethod


class IEvaluator(metaclass=ABCMeta):
    def __init__(self, solution):
        self._solution = solution

    @abstractmethod
    def get_solution(self):
        raise NotImplementedError


    @abstractmethod
    def evaluate(self, guess):
        raise NotImplementedError()
        