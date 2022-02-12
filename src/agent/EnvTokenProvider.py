from src.agent.interfaces.ITokenProvider import ITokenProvider
from dotenv import load_dotenv
from definitions import Constants as c
import os
import traceback


class EnvTokenProvider(ITokenProvider):
    def __init__(self, namespace=None, entry=None, password=None):
        super(EnvTokenProvider, self).__init__(namespace, entry, password)

    def register(self):
        try:
            load_dotenv()
        except Exception as e: 
            traceback.print_exc()


    def get_token(self):
        try:
            return os.environ.get(c.ENTRY)
        except Exception as e: 
            traceback.print_exc()