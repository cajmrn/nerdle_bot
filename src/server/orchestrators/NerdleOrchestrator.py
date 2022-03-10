from src.server.interfaces.IOrchestrator import IOrchestrator
from src.utils import utils as ut

class NerdleOrchestrator(IOrchestrator):
    def __init__(self, evaluator=None, generator=None, responder=None, transcriber=None, logger=None ) -> None:
        super(NerdleOrchestrator, self).__init__(evaluator, generator, responder, transcriber, logger)

    def generate_id(self):
        self._id = ut.generate_uuid()
        return self._id
    
    def evaluate(self, **generic):
        return self._evaluator.evaluate(**generic)

    def generate(self):
        return self._generator.generate()

    def respond(self):
        return self._responder.respond()

    def transcribe(self, **generic):
        return self._transcriber.transcribe(**generic)

    def log(self):
        return f'not implemented yet, not sure if necessary'