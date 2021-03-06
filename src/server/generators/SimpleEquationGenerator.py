import traceback
from src.server.interfaces.IGenerator import IGenerator


class SimpleEquationGenerator(IGenerator):
    '''
    #DEV THOUGHS
    SimpleEquationGenerator is a generator that has an easier disposition.
    the intention is to be able to create multiple generators for variable difficulty dispositions.
    '''
    def __init__(self, id=None,  mask=None, logger=None):
        super(SimpleEquationGenerator, self).__init__(id, mask, logger)
        self._equation = []

    def set_id(self, id):
        self._id = id
        
    def generate(self):
        '''
        #DEV THOUGHTS
        considering returning a simple string that can be sent to eval("expression") to check if expression is valid.
        that way we cimcumvent having to pull all values out of the array first... just a thought, it's not an expensive
        opeation. 
        will it complicate equation generation? don't think so 
        '''
        try:
            self._equation = ['2','+','3','*','4','=',14]
            self._logger.set_source(str(__class__.__name__))
            self._logger.log(self._logger.format(self._equation))

            return self._equation
        except Exception as e:
            traceback.print_exc()

        

