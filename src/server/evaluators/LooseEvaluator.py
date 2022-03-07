from typing import Tuple
from src.server.interfaces.IEvaluator import IEvaluator


class LooseEvaluator(IEvaluator):
    '''
    Allows for the creation of multiple evaluators with different dispositions. 
    Can be as strict as you like.
    '''
    def __init__(self, id=None, solution=None, logger=None):
        super(LooseEvaluator, self).__init__(id, solution, logger)

    def set_solution(self, s):
        self._solution = s

    def evaluate(self, guess) -> Tuple[int, dict]:
        '''
        be sure to run set_solution() with the value generated from the generator 
        evaluates the guess against the solution.
        Uses the numerical value to pull a response from the library 
        eventually used in the responder as 
            def get_response(self):
                return self.library[self._evaluation]
        '''
        print(f'your guess was {guess} and the solution is {self._solution}')
        '''
        Wondering about this implementation. Not sure if it's working right is seems so
        the implementation is:
        iterate through your guess and take each value and compare it to what the solution is.
        if the two values match in placement and value give a value of 4
        if the two don't match but the guess is in the solution give a value of 2
        if the value is not in the solution give a value of 1
        return the sum of the values in the dictionary 
        '''

        i= 0
        for i in range(len(guess)):
            for j in range(i, len(self._solution)):
                if guess[i] == self._solution[j]:
                    self._guess_set[i] = 4
                    break
                elif guess[i] in self._solution:
                    self._guess_set[i] = 2
                    break
                else:
                    self._guess_set[i] = 1
                    #break
        
        return sum(self._guess_set.values()), self._guess_set