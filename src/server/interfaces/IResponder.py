from abc import ABCMeta, abstractmethod


class IResponder(metaclass=ABCMeta):
    def __init__(self, library):
        self._library = library

    @abstractmethod
    def get_response(self):
        raise NotImplementedError()


    @abstractmethod
    def send_response(self):
        raise NotImplementedError()

    