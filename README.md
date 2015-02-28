#Experiments with Wowee's MIP

##Introduction
This started out as a reverse engineering effort to work out the protocol used by Wowwee's MIP robot. I used an Ubertooth One to sniff the Bluetooth Low Energy traffic and worked out some of the commands to control the robot. After posting a script on Git Hub, I emailed Wowwee asking about additional documentation. Andy, the R&D Software Manager at Wowwee got back to me and within a few days they posted [documentation] (https://github.com/WowWeeLabs/MiP-BLE-Protocol/blob/master/MiP-Protocol.md) on their Git Hub site. Fantastic! Thanks Wowwee!

So this is no longer about reverse engineering the MIP and more about providing an easy way to drive the MIP using Python.

##Getting Started - Linux
You need a computer with Bluetooth 4.0 capability, or a Bluetooth 4.0 dongle. I'm using a $4 USB dongle I picked up on ebay. It shows up like this in Linux:

```
$ lsusb
Bus 003 Device 002: ID 0a12:0001 Cambridge Silicon Radio, Ltd Bluetooth Dongle (HCI mode)
```

You need a recent version of bluez installed. In particular, you need hcitool and gatttool. Install bluez 5.23 or greater. If you're on Fedora 20 or 21, you'll need to build it yourself. This [bug report] (https://bugzilla.redhat.com/show_bug.cgi?id=1141909) is probably of interest.

Use hcitool to confirm that the interface is ready to go:
	
```
$ hcitool dev
Devices:
	hci0	00:B4:7D:E2:A1:FE
```

... so I'm going to use the bluetooth interface hci0 to look for MIP.

Turn MIP on and search for it (you'll probably have to sudo):

```
$ sudo hcitool -i hci0 lescan
LE Scan ...
D0:39:72:B8:C5:84 (unknown)
D0:39:72:B8:C5:84 WowWee-MiP-33506
```

Grab the bluetooth address of MIP (in this case, D0:39:72:B8:C5:84). Time to start the script:

```
$ ./src/examples/turtle_example.py -i hci0 -b D0:39:72:B8:C5:84
```

You should see MIPs chest light turn green when the bluetooth connection is made. MIP will make a sound and move around.

