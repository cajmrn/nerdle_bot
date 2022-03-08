import traceback
import uuid

class utils():
    @staticmethod
    def parse_guess(guess, prefix)-> list:
        try:
            if prefix:
                return guess.split(prefix, maxsplit=1)[1]
        except Exception as e:
            traceback.print_exc()
    
    @staticmethod
    def generate_uuid():
        try:
            return str(uuid.uuid4())
        except Exception as e:
            traceback.print_exc()
        