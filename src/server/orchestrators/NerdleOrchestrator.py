from interfaces import IOrchestrator

class NerdleOrchestrator(IOrchestrator):
    def __init__(self, evaluator, generator, responder ) -> None:
        super(NerdleOrchestrator).__init__(evaluator, generator, responder)

    def evaluate(self):
        self._evaluator.evaluate()

    def generate(self):
        self._generator.generate()

    def responder(self):
        self._responder.respond()