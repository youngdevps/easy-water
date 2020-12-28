import flow_metter_control
import time
import os

print("===================1================")
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
from mfrc522 import SimpleMFRC522

print("===================2================")
reader = SimpleMFRC522()
on = False
oldId = ""
print("===================3================")
gapElapsedTime = 2.2
flow_metter_control.setup()

"""
while True:
    print("===================4================")
    try:
        id, text = reader.read()
        flow_metter_control.setup()
        if on == True:
            print("===================5================")
            if str(oldId) == str(id):
                print("===================6================")
                on = False
                # write the final flow to tag
                flow_metter_control.stop_flow_counter()
                print("===================7================")
        else:
            print("===================9================")
            on = True
            oldId = str(id)
            flow_metter_control.start_flow_counter2()
            print("===================10================")
    except:
        print("************* out of reading tag")
 
print("===================11================")  
"""

while True:
    print("===================4================")
    id, text = reader.read()
     print("===================the id is id_: {}================".format(id))
    time.sleep(gapElapsedTime)
    if on == True:
        print("===================5================")
        if str(oldId) == str(id):
            print("===================6================")
            on = False
            # write the final flow to tag
            count, flow = flow_metter_control.stop_flow_counter()
            time.sleep(gapElapsedTime)
            print("///////////count:{} and flow:{}/////////////////".format(count, flow))
            flow_metter_control.resetCountAndFlow()
            print("===================7================")
    else:
        print("===================8================")
        on = True
        oldId = str(id)
        flow_metter_control.start_flow_counter2()
        flowToReach = 1
        hasReached = False
        while hasReached is False:
            count, flow = flow_metter_control.stop_flow_counter()
            print("::::::::::::: the flow is ", flow)
            if flow == flowToReach:
                hasReached = True
        print("===================9================")
 
print("===================10================")  