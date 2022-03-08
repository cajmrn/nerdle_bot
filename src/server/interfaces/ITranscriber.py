from abc import ABCMeta, abstractmethod


class ITranscriber(metaclass=ABCMeta):
    def __init__(self, id, vocab, logger) -> None:
        self._id = id
        self._logger = logger
        self._vocab = vocab
        self._transcribed_set= []

    @abstractmethod
    def transcribe(self, evalution_set)-> list:
        raise NotImplementedError()

    # @abstractmethod
    # def log(self):
    #     raise NotImplementedError()