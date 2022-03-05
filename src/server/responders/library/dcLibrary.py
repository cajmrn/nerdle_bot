from inspect import trace
import traceback

class library():

    def __init__(self, db, name) -> None:
        self._db = db
        self._name = name
        

    def add_library(self, lib):
        try:
            self._db.add(self._name, lib)
        except Exception as e: 
            traceback.print_exc()


    def delete_library(self):
        try:
            self._db.delete(self._name, None)
        except Exception as e:
            traceback.print_exc()

    def update_entry(self, key, value):
        try: 
            lib = self._db.get(self._name)
            lib[key] = value
            self._db.update(self._name, lib)
            lib = None

        except Exception as e: 
            traceback.print_exc() 

    def get_library(self):
        try:
            return self._db.get(self._name)[0]
        except Exception as e:
            traceback.print_exc()