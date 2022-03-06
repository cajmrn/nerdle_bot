from abc import ABCMeta, abstractmethod


class ILogger(metaclass=ABCMeta):
    def __init__(self, id, src, dest):
        self._id = id
        self._src = src
        self._dest = dest

    @abstractmethod
    def format(self, s):
        raise NotImplementedError()   

    @abstractmethod
    def log(self, msg):
        raise NotImplementedError()