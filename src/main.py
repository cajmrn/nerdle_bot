from src.agent.nerdle_agent import NerdleAgent
from src.agent.EnvTokenProvider import EnvTokenProvider

import definitions as d
import os


if __name__ == '__main__':

    etp = EnvTokenProvider()
    etp.register()

    na = NerdleAgent()
    na.run(etp.get_token())

