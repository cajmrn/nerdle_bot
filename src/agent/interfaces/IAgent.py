from abc import ABCMeta, abstractmethod

class IAgent(metaclass=ABCMeta):
    def __init__(self, token):
        self._token = token
        self._msg = ''

    @abstractmethod
    def get_response(self):
        raise NotImplementedError()
        