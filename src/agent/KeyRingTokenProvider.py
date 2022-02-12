from src.agent.interfaces.ITokenProvider import ITokenProvider
import keyring
import keyring.util.platform_ as keyring_platform
import traceback


class KeyRingTokenProvider(ITokenProvider):
    def __init__(self, namespace=None, entry=None, password=None):
        super(KeyRingTokenProvider, self).__init__(namespace, entry, password)


    def register(self):
        try:
            keyring.set_password(self._namespace, self._entry, self._password)
        except Exception as e: 
            traceback.print_exc()


    def get_token(self):
        try:
            return keyring.get_credential(self._namespace, self._entry)
        except Exception as e: 
            traceback.print_exc()
