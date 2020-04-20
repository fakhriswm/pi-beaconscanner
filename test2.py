n = 5

beacon0 = {"major":111, "minor":1234, "rssi":-70}
beacon1 = {"major":111, "minor":4321, "rssi":-75}
beacon2 = {"major":111, "minor":5678, "rssi":-70}
beacon3 = {"major":111, "minor":8765, "rssi":-75}
beacon4 = {"major":111, "minor":9876, "rssi":-70}

beacon = {}
beaconList = {}

for i in range(n):
	if i==0:
		beacon = beacon0
	if i==1:
		beacon = beacon1
	if i==2:	
		beacon = beacon2	
	if i==3:
		beacon = beacon3
	if i==4:
		beacon = beacon4
	
	beaconList[i] = beacon
print "len",len(beaconList)
for i in range(n):
	print i, beaconList[i]
	#print(beaconList[i]['major'])
	#print(beaconList[i]['minor'])
	#print(beaconList[i]['rssi'])

del beaconList[2]

print "len",len(beaconList)

print "result"

for i in beaconList:
	print i, beaconList[i]
	#print(beaconList[i]['major'])
	#print(beaconList[i]['minor'])
	#print(beaconList[i]['rssi'])
