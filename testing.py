import ScanUtility
import bluetooth._bluetooth as bluez

#Set bluetooth device. Default 0.
dev_id = 0
txpower = -59

def get_distance(rssi):
        ratio = (rssi*1.0)/txpower
        if ratio < 1.0:
               return pow(ratio,10)
        else:
        	dist = (0.89976)*pow(ratio,7.7095)+0.111
        	return dist

try:
	sock = bluez.hci_open_dev(dev_id)
	print ("\n *** Looking for BLE Beacons ***\n")
	print ("\n *** CTRL-C to Cancel ***\n")
except:
	print ("Error accessing bluetooth")

ScanUtility.hci_enable_le_scan(sock)
#Scans for iBeacons
try:
	while True:
		returnedList = ScanUtility.parse_events(sock, 10)
		rssi = int(returnedList["rssi"])
		distance = get_distance(rssi)
		print "scan", returnedList, "distance|", distance
		
except KeyboardInterrupt:
    pass
