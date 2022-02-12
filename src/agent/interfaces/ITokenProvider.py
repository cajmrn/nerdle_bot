from abc import ABCMeta, abstractclassmethod, abstractmethod

class ITokenProvider(metaclass=ABCMeta):
    def __init__(self, namespace=None, entry=None, password=None):
        self._namespace = namespace
        self._entry = entry
        self._password = password

    @abstractmethod
    def register(self):
        raise NotImplementedError()

    @abstractmethod
    def get_token():
        raise NotImplementedError()