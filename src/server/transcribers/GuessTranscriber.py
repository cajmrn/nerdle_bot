import traceback
from src.server.interfaces.ITranscriber import ITranscriber



class GuessTranscriber(ITranscriber):
    def __init__(self, id=None, vocab=None, logger=None):
        super(GuessTranscriber, self).__init__(id, vocab, logger)

    def transcribe(self,**generic):
        '''
        given an evaluation set returned from an evaluator in format {index_of_guess:point_value, ...} 
        iterate through the values and grab an associated value from the vocab returned from MikeDB.
        '''
        evaluation_set = generic['evaluation_set']
        is_generator = generic['is_generator']
        self._transcribed_set = []
        try: 
            if is_generator:
                for i in evaluation_set.values():
                    self._transcribed_set.append(self._vocab[str(1)])
            else:
                for i in evaluation_set.values():
                    self._transcribed_set.append(self._vocab[str(i)])
              
            return self._transcribed_set
        except Exception as e: 
            traceback.print_exc()
