import traceback

class vocabulary():

    def __init__(self, db, name) -> None:
        self._db = db
        self._name = name
        
    def add_vocabulary(self, vocab):
        try:
            self._db.add(self._name, vocab)
        except Exception as e: 
            traceback.print_exc()


    def delete_vocabulary(self):
        try:
            self._db.delete(self._name, None)
        except Exception as e:
            traceback.print_exc()

    def update_entry(self, key, value):
        try: 
            vocab = self._db.get(self._name)[0]
            vocab[key] = value
            self._db.update(self._name, vocab)
            vocab = None
        except Exception as e: 
            traceback.print_exc() 

    def get_vocabulary(self):
        try:
            return self._db.get(self._name)[0]
        except Exception as e:
            traceback.print_exc()