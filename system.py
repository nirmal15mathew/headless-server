import RPi.GPIO as GPIO
from utils import EventManager, SecurityAndAuthentication, SensorDataCompiler, Server, DBManager
credentials = {}

class System:
    def __init__(self) -> None:
        self.event_manager = EventManager.EventManager(self)
        self.security = SecurityAndAuthentication.SecurityHandler(self)
        self.data_compiler = SensorDataCompiler.DataCompiler(self)
        self.server = Server.Server(self)
        self.db = DBManager.get_db(credentials)
        self.pins = DBManager.get_pins(self.db)
        self.run = True

    
    def setup(self):
        # self.startServer()
        GPIO.setmode(GPIO.BOARD)

        for pin in self.pins:
            GPIO.setup(pin.number, pin.mode)



    def start(self):
        self.server.start()
        while self.run:
            self.execute_behaviours()


    def cleanup(self):
        GPIO.cleanup()

    def execute_behaviours(self):
        self.data_compiler.useData([pin for pin in self.pins if pin.mode == "INPUT"])
        
