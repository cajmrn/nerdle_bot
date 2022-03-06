from abc import ABCMeta, abstractmethod


class ILogger(metaclass=ABCMeta):
    def __init__(self, src, dest):
        self._src = src
        self._dest = dest

    @abstractmethod
    def fromat(self):
        raise NotImplementedError()   

    @abstractmethod
    def log(self):
        raise NotImplementedError()