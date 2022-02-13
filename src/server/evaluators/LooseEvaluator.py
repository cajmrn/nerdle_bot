from src.server.interfaces.IEvaluator import IEvaluator


class LooseEvaluator(IEvaluator):
    '''
    Allows for the creation of multiple evaluators with different dispositions. 
    Can be as strict as you like.
    '''
    def __init__(self, solution):
        super(LooseEvaluator, self).__init__(solution=None)

    def get_solution(self):
        return self._solution

    def evaluate(self, guess):
        '''
        evaluates the guess against the solution.
        Uses the numerical value to pull a response from the library 
        eventually used in the responder as 
            def get_response(self):
                return self.library[self._evaluation]
        '''
        print(f'your guess was {guess} and the solution is {self._solution}')
        
        return 1