from src.agent.nerdle_agent import NerdleAgent
from src.agent.EnvTokenProvider import EnvTokenProvider
from src.server.generators.SimpleEquationGenerator import SimpleEquationGenerator
from src.server.evaluators.LooseEvaluator import LooseEvaluator
from src.server.responders.NerdleResponder import NerdleResponder
from src.server.responders.library.dcLibrary import library


import definitions as d
import os

'''
Currently just using main for testing.
'''
if __name__ == '__main__':

    seg = SimpleEquationGenerator()
    an_eq = seg.generate()

    le = LooseEvaluator(an_eq)
    #will need to figure out how to get the guess from nerdleagent probable if it has a prefix of $cast
    score = le.evaluate('')

    #instantiate a library to get all repsonses. 
    responses = library._library

    nr = NerdleResponder(responses)
    nerdle_resposne = nr.get_response(score)

    etp = EnvTokenProvider()
    etp.register()

    na = NerdleAgent()
    
    na.run(etp.get_token())

