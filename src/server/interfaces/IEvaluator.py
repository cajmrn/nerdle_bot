from abc import ABCMeta, abstractmethod


class IEvaluator(metaclass=ABCMeta):
    def __init__(self, id, solution, logger):
        self._id = id
        self._logger = logger
        self._solution = solution

    @abstractmethod
    def set_solution(self):
        raise NotImplementedError()

    @abstractmethod
    def evaluate(self, guess):
        raise NotImplementedError()

    @abstractmethod
    def log(self):
        raise NotImplementedError()

        