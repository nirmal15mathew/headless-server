class DataCompiler:
    def __init__(self, system) -> None:
        self.system = system
        self.channels = {}

    
    def addChannel(self, name, channel):
        self.channels[name] = channel
    
    def setupCompilation(self, name, func):
        func(self.channels[name], self.system.logger)


class Channel:
    def __init__(self) -> None:
        self.data = None

    def getDataStream(self):
        return self.data
    
    def bindData(self, source):
        self.data = source.data