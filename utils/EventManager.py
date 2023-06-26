class Event:
    def __init__(self, name: str,handler, level: int = 999) -> None:
        self.name = name
        self.handler = handler
        self.listeners = []
        self.level = level

    def stop(self):
        self.handler.stopPropagation(self)

    def addListener(self, func):
        self.listeners.append(func)

    def propagate(self, data):
        sortedList = sorted(self.listeners, reverse=True)
        for listener in sortedList:
            listener(data)

class EventManager:
    def __init__(self, system) -> None:
        self.events = []
        self.system = system

    def stopPropagation(self, event: Event):
        if event in self.events:
            self.events.remove(event)
    
    def createEvent(self, name):
        self.events.append(Event(name, self))
        return self.events[-1]
    
    def propagateEvent(self, name, data):
        for event in self.events:
            if event.name == name:
                event.propagate(data)


if __name__ == '__main__':
    def testFunc(data):
        print(data)
    electricalEvents = EventManager()
    pwr = electricalEvents.createEvent("power-on")
    pwr.addListener(testFunc)
    pwr.propagate("voltage: 230")
        
