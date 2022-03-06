from src.server.interfaces.ILogger import ILogger

class GeneratorLogger(ILogger):

    def __init__(self, id=None, src=None, dest=None ):
        super(GeneratorLogger, self).__init__(id, src, dest)

    def set_id(self, id):
        self._id = id

    def set_source(self, s):
        self._src = s

    def format(self, s) -> str:
        return f'{__class__.__name__} - ORCHESTRATOR[{self._id}]:: {self._src} generated equation:' + str(s)

    def log(self, msg) -> None:
        self._dest.add(key= self._id, value=msg)