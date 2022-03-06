from src.server.interfaces.ILogger import ILogger

class GeneratorLogger(ILogger):
    '''
    Implemented our own logging to MikeDB, KISS for the sake of this implementation.
    the ID that we use here is the Orchestrator id (using generate_id) this will in general be the game id that will be used throughout the application.
    '''
    def __init__(self, id=None, src=None, dest=None ):
        super(GeneratorLogger, self).__init__(id, src, dest)
    
    def set_id(self, id):
        '''
        As a composite we run into the issue where at Instantiation the orchestrator ID has not been generated. 
        Need a function to set the id that we got from generate_id be sure that Orchestrator.generate_id() has been run.
        '''
        self._id = id
    
    def set_source(self, s):
        '''
        Again as a composite, in order to capture the class that generating the log,
        this method must be run from originating class. prior to running format() and log()
        '''
        self._src = s

    def format(self, s) -> str:
        '''
        takes a string and appends it to the  logger name and the orchestrator generated game id.
        '''
        return f'{__class__.__name__} - ORCHESTRATOR[{self._id}]:: {self._src} generated equation:' + str(s)

    def log(self, msg) -> None:
        '''
        logs the message to MikeDB all keys will be the game id
        '''
        self._dest.add(key= self._id, value=msg)