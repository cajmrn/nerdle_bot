import traceback
from src.server.interfaces.IGenerator import IGenerator


class EquationGenerator(IGenerator):
    def __init__(self, mask):
        super(EquationGenerator, self).__init__(mask)
        self._equation = []


    def generate(self):
        try:
            self._equation = [2,'+',3,'*',4,'=',14]
        except Exception as e:
            traceback.print_exc()

        return self._equation
