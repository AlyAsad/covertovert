from scapy.all import IP, ICMP, send

# Implement your ICMP sender here


packet = IP(dst="receiver", ttl=1) / ICMP()

send(packet, verbose = False)