import traceback
from src.server.interfaces.ITranscriber import ITranscriber



class DiscordTranscriber(ITranscriber):
    def __init__(self, id=None, vocab=None, logger=None):
        super(DiscordTranscriber, self).__init__(id, vocab, logger)

    def transcribe(self, evaluation_set: dict):
        '''
        given an evaluation set returned from an evaluator in format {index_of_guess:point_value, ...} 
        iterate through the values and grab an associated value from the vocab returned from MikeDB.
        '''
        try: 
            for i in evaluation_set.values():
                self._transcribed_set.append(self._vocab[str(i)])
            
            return self._transcribed_set
        except Exception as e: 
            traceback.print_exc()
