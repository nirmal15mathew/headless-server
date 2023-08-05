import RPi.GPIO as GPIO
from firebase_admin import firestore, initialize_app, credentials
import threading
from time import sleep

# Globals
RUN = True
LED_PIN = 13
PIN_VAL = 0
BOARD_STATE = {}
IS_INITIALISED = False

# setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

def initialize_pin(pin_id, pin_mode):
    if (pin_mode == "OUTPUT"):
        GPIO.setup(pin_id, GPIO.OUT)
        pass
    elif (pin_mode == "INPUT"):
        GPIO.setup(pin_id, GPIO.IN)
        pass

    print("pin_id: ", pin_id, " has been initialized with mode: ", pin_mode)

def set_pin_state_binary(pin_id, pin_state):
    if (pin_state == 1):
        GPIO.output(pin_id, GPIO.HIGH)
        pass
    elif (pin_state == 0):
        GPIO.output(pin_id, GPIO.LOW)
        pass
    print("Pin no: ", pin_id, " has been set to: ", pin_state)

def read_pin_state(pin_id):
    return GPIO.input(pin_id)

def update_read_values(pin_id, pin_state):
    pass

def set_pin_state_analog(pin_id, pin_state):
    pass
    

try:
    creds = credentials.Certificate('./assets/serviceAccount.json')
    app = initialize_app(creds)
    db = firestore.client()

    # Create an Event for notifying main thread.
    callback_done = threading.Event()
    
    # Create a callback on_snapshot function to capture changes
    def on_snapshot(doc_snapshot, changes, read_time):
        
        for doc in doc_snapshot:
            doc_ref = doc.to_dict()

            # initialising the board if not initialised 
            if "status" in doc_ref:
                pass
            else:
                # setting the values for the pins
                set_pin_state_binary(pin_id=doc.id, pin_state=doc_ref["value"])
                global IS_INITIALISED
                if not IS_INITIALISED:
                    initialize_pin(pin_id=doc.id, pin_mode=doc_ref["mode"])

        
        IS_INITIALISED = True
                
        callback_done.set()
    
    doc_ref = db.collection("board01")
    
    # Watch the document
    doc_watch = doc_ref.on_snapshot(on_snapshot)


    while RUN:
        """Simple blink program"""
        # GPIO.output(LED_PIN, PIN_VAL) # turns the pin to high

except KeyboardInterrupt:
    print("Exiting...")
    # GPIO.cleanup()