from src.server.interfaces.IResponder import IResponder


class NerdleResponder(IResponder):
    def __init__(self, evaluation=None, library=None):
        super(NerdleResponder, self).__init__(evaluation, library)

    def get_response(self):
        return self.library[self._evaluation]