import clr
import sys
import time
import platform
#dependencies  32 bit python, pythonnet

#this was tested with a single U1816E switch box you can run more than 1 just use the instrument list and tease out the model and serial number pairs for each

#Tim Fairfield Keysight  Oct 17 2022
#tested with python 3.8.3
#('32bit', 'WindowsPE')
# make ure you are using 32 bit Python and that pythonnet is installed i.e pip install pythonnet
#if either of these are not met you will get a missing clr reference

def getSwitchpositions():
    #this gets the positions of the switches , a tuple of 3 is returned I ignore the first position (I dont know what it means to be honest)
    position = obj.GetRFPath2(0, 0)
    print(f"switch settings sw1:{position[1]}  sw2:{position[2]}")
#get platform info, this helps to make sure your dll is 32 bit you can leave this code out if you want
print(platform.python_version())
print(platform.architecture())

locationofDLL='D:\documents m2\code\python projects\u1816eswitchexample'
sys.path.append(locationofDLL)
clr.AddReference('Agilent.U1816x')
#if you get an error here make sure your python is 32 bit AND (if you arent using IronPython) that you pip installed pythonnet
from Agilent.U1816x import *

#must reference as an object to access commands
obj =AgU1816x()

'''you can peek at the object to see commands but here is a list
Use the Windows dll documentation for more info but some basic uses are below

AutoCycling = {MethodBinding} <bound method 'AutoCycling'>
ClearRelayCount = {MethodBinding} <bound method 'ClearRelayCount'>
Close = {MethodBinding} <bound method 'Close'>
CyclingControlState = {MethodBinding} <bound method 'CyclingControlState'>
Equals = {MethodBinding} <bound method 'Equals'>
Finalize = {MethodBinding} <bound method 'Finalize'>
GetCyclingControlState = {MethodBinding} <bound method 'GetCyclingControlState'>
GetHashCode = {MethodBinding} <bound method 'GetHashCode'>
GetRFPath = {MethodBinding} <bound method 'GetRFPath'>
GetRFPath2 = {MethodBinding} <bound method 'GetRFPath2'>
GetRelayCount = {MethodBinding} <bound method 'GetRelayCount'>
GetType = {MethodBinding} <bound method 'GetType'>
Initialize = {MethodBinding} <bound method 'Initialize'>
InstrumentFirmwareRevision = {MethodBinding} <bound method 'InstrumentFirmwareRevision'>
InstrumentList = {MethodBinding} <bound method 'InstrumentList'>
InstrumentModel = {MethodBinding} <bound method 'InstrumentModel'>
MemberwiseClone = {MethodBinding} <bound method 'MemberwiseClone'>
Overloads = {ConstructorBinding} Agilent.U1816x.AgU1816x()
RFPATH = {MethodBinding} <bound method 'RFPATH'>
RFPATH2 = {MethodBinding} <bound method 'RFPATH2'>
ReferenceEquals = {MethodBinding} <bound method 'ReferenceEquals'>
SerialNumber = {MethodBinding} <bound method 'SerialNumber'>
StatusEnum = {CLR Metatype} <class 'Agilent.U1816x.StatusEnum'>
ToString = {MethodBinding} <bound method 'ToString'>

'''

#to do anything you must initialize it, be aware you may have more than one switch, this example only shows one switch
instlist=obj.InstrumentList()

print(f"instruments found [model,serial]: {instlist}")
#pick the first instrument in the list (we are only showing access to one switch box here)
model= instlist[0].split(',',1)[0]
serial= instlist[0].split(',',1)[1]

#when you access a switch box you need to specify model and serial
obj.Initialize(model,serial)
#you should get an output similar to this
# >instruments found [model,serial]: ['U1816E,MY641410001']

#this is the walking through of all switches startup test, helps identify things are running
#you can comment out in a real use case
print ("Running auto cycle test...")
obj.AutoCycling()
#test 1 set both switches to 1
sw1,sw2=1,1
obj.RFPATH2(sw1,sw2)
getSwitchpositions()
#you should get an output similar to this
# >switch settings sw1:1  sw2:1

#test2 change switches
time.sleep(1)
sw1,sw2=6,4
obj.RFPATH2(sw1,sw2)
getSwitchpositions()

