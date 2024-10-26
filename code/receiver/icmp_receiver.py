from scapy.all import ICMP, IP, sniff

# Implement your ICMP receiver here

waiting = True

def handle_packet(packet):
    global waiting
    if packet.haslayer(ICMP) and packet[IP].ttl == 1:
        waiting = False
        packet.show()

while waiting:
    sniff(filter="icmp", prn=handle_packet, count = 1)


