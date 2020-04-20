import RPi.GPIO as GPIO 
import json 
import ScanUtility 
import bluetooth._bluetooth as bluez 
from time import sleep 
import time
import Tkinter

top = Tkinter.Tk()
top.mainloop()

servoPIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with $
p.start(2.5) # Initialization

#Set bluetooth device. Default 0.
dev_id = 0
bletype = ""
beaconType = "iBeacon"
txpower = -59
distance_limit = 1.5
numb_ofbeacon = 10
detect = 5
newcome = True
timedelay = 7000
beacon_filter = "cb"

beacon = {}
beaconList = {}
returnedList = {}


try:
	sock = bluez.hci_open_dev(dev_id)
	print ("\n *** Looking for BLE Beacons ***\n")
	print ("\n *** CTRL-C to Cancel ***\n")
except:
	print ("Error accessing bluetooth")

ScanUtility.hci_enable_le_scan(sock)

def get_distance(rssi):
	ratio = (rssi*1.0)/txpower
	if ratio < 1.0:
   		return pow(ratio,10)
	else:
		return (0.89976)*pow(ratio,7.7095)+0.111

#Scans for iBeacons
try:
	while True:

		returnedList = ScanUtility.parse_events(sock, 10)
		bletype = returnedList['type']
		try :
			uuid = returnedList['uuid']
		except :
			break
		millisecond = int(round(time.time()*1000))
		if bletype == beaconType and uuid[0:2] == beacon_filter:
			major = returnedList['major']
			rssi = int(returnedList['rssi'])
			distance = get_distance(rssi)
			if distance <= distance_limit:
				uuid = returnedList['uuid']
				minor = returnedList['minor']
				newcome = True
				print "beacon", minor, distance
				if len(beaconList):
					for x in beaconList:
						#print "loop",x
						if beaconList[x]['minor'] == minor:
							newcome = False
							#print "registered",minor,x
							counter = beaconList[x]['counter']
							beaconList[x]['millis'] = millisecond
							beaconList[x]['distance'] = distance
							beaconList[x]["rssi"] = rssi
							if counter == detect:
								print "access granted"
								p.ChangeDutyCycle(7.5)
								time.sleep(2)
								p.ChangeDutyCycle(0.5)
							counter+=1
							beaconList[x]['counter']=counter

				if newcome == True and len(beaconList) < numb_ofbeacon:
					beacon = {"uuid":uuid,"major":major,"minor":minor,"rssi":rssi,"distance":distance,"millis":millisecond, "counter":1}
					beaconList[len(beaconList)] = beacon
					#print "add new beacon :", beacon, len(beaconList)
					print "add new : " , minor

		#print "len", len(beaconList)	
		#if len(beaconList) > 0:
			for x in beaconList:
				timestamp = beaconList[x]['millis']
				minor = beaconList[x]['minor']
				counter = beaconList[x]['counter']
				if millisecond-timestamp >= timedelay:
					print "expired", minor
					del beaconList[x]
					break
				else:
					print "inrange", minor, counter,millisecond,timestamp

except KeyboardInterrupt:
    pass
