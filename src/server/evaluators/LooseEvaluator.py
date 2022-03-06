from src.server.interfaces.IEvaluator import IEvaluator


class LooseEvaluator(IEvaluator):
    '''
    Allows for the creation of multiple evaluators with different dispositions. 
    Can be as strict as you like.
    '''
    def __init__(self, solution=None):
        super(LooseEvaluator, self).__init__(solution)

    def set_solution(self, s):
        self._solution = s

    def evaluate(self, guess):
        '''
        be sure to run set_solution() with the value generated from the generator 
        evaluates the guess against the solution.
        Uses the numerical value to pull a response from the library 
        eventually used in the responder as 
            def get_response(self):
                return self.library[self._evaluation]
        '''
        print('your guess was {guess} and the solution is {self._solution}')
        
        return 1