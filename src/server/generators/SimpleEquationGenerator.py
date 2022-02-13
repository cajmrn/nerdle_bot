import traceback
from src.server.interfaces.IGenerator import IGenerator


class SimpleEquationGenerator(IGenerator):
    '''
    #DEV THOUGHS
    SimpleEquationGenerator is a generator that has an easier disposition.
    the intention is to be able to create multiple generators for variable difficulty dispositions.
    '''
    def __init__(self, mask=None):
        super(SimpleEquationGenerator, self).__init__(mask)
        self._equation = []


    def generate(self):
        '''
        #DEV THOUGHTS
        considering returning a simple string that can be sent to eval("expression") to check if expression is valid.
        that way we cimcumvent having to pull all values out of the array first... just a thought, it's not an expensive
        opeation. 
        will it complicate equation generation? don't think so 
        '''
        try:
            self._equation = [2,'+',3,'*',4,'=',14]
        except Exception as e:
            traceback.print_exc()

        return self._equation
