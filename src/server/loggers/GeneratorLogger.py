from src.server.interfaces.ILogger import ILogger


class GeneratorLogger(ILogger):
    def __init__(self,src, dest) -> None:
        super(GeneratorLogger).__init__(src, dest)

    def format(self):
        pass

    def log(self):
        pass