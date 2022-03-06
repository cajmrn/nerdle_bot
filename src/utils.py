import traceback

class utils():
    @staticmethod
    def parse_guess(guess, prefix)-> list:
        try:
            if prefix:
                return guess.split(prefix, maxsplit=1)[1]
        except Exception as e:
            traceback.print_exc()
        