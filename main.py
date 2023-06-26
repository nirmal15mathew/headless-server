import RPi.GPIO as GPIO
from firebase_admin import firestore, initialize_app, credentials
import threading
from time import sleep
import os

# Globals
RUN = True
LED_PIN = 13
PIN_VAL = 0
BOARD_STATE = {}
IS_INITIALISED = False

# setup
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(LED_PIN, GPIO.OUT)

def set_board_state(state_dict):
    document_list = list(state_dict.keys())
    __dict__.

    for doc in document_list:
        if state_dict[doc].mode == "OUTPUT":
            if 

def initialise_board(state):
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
            if doc.id == str(LED_PIN):
                BOARD_STATE = doc.to_dict()
                if not IS_INITIALISED:
                    initialise_board(BOARD_STATE)
                else:
                    set_board_state(BOARD_STATE)
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