from http.client import responses
# from src.agent.nerdle_agent import NerdleAgent
# from src.agent.test_agent import TestAgent
# from src.agent.EnvTokenProvider import EnvTokenProvider
from src.server.generators.SimpleEquationGenerator import SimpleEquationGenerator
from src.server.evaluators.LooseEvaluator import LooseEvaluator
from src.server.loggers.GeneratorLogger import GeneratorLogger
from src.server.orchestrators.NerdleOrchestrator import NerdleOrchestrator
# from src.server.responders.NerdleResponder import NerdleResponder
from src.server.responders.library.dcLibrary import library
from src.server.db.DbConfig import DB_CONFIG
from src.server.db.MikeDB import MikeDB


import definitions as d
import os

'''
Currently just using main for testing.
'''
if __name__ == '__main__':

    # #seg = SimpleEquationGenerator()
    # #an_eq = seg.generate()
    solution = [1,'+',2,'+',3,'=', 6]
    le = LooseEvaluator(solution=solution)
    guess = [1,'+',2,'+',3,'=', 6]
    guess.reverse()
    print(guess)
    #_sum , eval_set = le.evaluate([2,'-',7,'/',9,'=', 1])
    _sum , eval_set = le.evaluate(guess=guess)
    print(f'_sum: {_sum}')
    print(f'eval_set: {eval_set}')

    vocab = {
        4:"::green_square::"
        ,2:"::purple_square::"
        ,1:"::white_square::"
    }

    # # #will need to figure out how to get the guess from nerdleagent probable if it has a prefix of $cast
    # # score = le.evaluate('')

    # # #instantiate a library to get all repsonses.
    # db = MikeDB(db_host=DB_CONFIG['DB_HOST'], db_name=DB_CONFIG['DB_NAME'], db_key=DB_CONFIG['DB_KEY'])
    # # _library = {
    # #     0:'That\'s correct you genius motherfucker!'
    # #     , 1:'Not even close dumbo'
    # #     , 2:'You are in no way closer to the solution... Idiot!'
    # #     } 

    # lb = library(db, 'meanie')
    # #lb.delete_library()
    # #lb.add_library(_library)

    # responses = lb.get_library()
    # # print(responses)

    # # nr = NerdleResponder(responses)
    # # # nerdle_resposne = nr.get_response(score)
    # g_logger = GeneratorLogger(dest=db)
    # se_generator = SimpleEquationGenerator(logger=g_logger)
    # n_orchestrator = NerdleOrchestrator(generator=se_generator)

    # game_id = n_orchestrator.generate_id()
    # print(game_id)

    # se_generator.set_id(game_id)

    # g_logger.set_id(game_id)

    # _eq = se_generator.generate()
    # print(_eq)

    # print(db.get(key=game_id))

    # # etp = EnvTokenProvider()
    # # etp.register()

    # # # na = NerdleAgent()
    
    # # # na.run(etp.get_token())

    # # ta = TestAgent(le, nr)
    # # ta.run(etp.get_token())

    

