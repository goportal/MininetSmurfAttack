import sys
from mininet.log import info, setLogLevel
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.util import dumpNodeConnections
from mininet.node import Controller, RemoteController, Node
from mininet.cli import CLI

# construct topology
class SingleSwitchTopo(Topo):

    def build(self, n=int(sys.argv[1])):
        switch = self.addSwitch('s1')
        for h in range(n):
            host = self.addHost('h%s' % (h + 1))
            self.addLink(host, switch)

def simpleTest():
    topo = SingleSwitchTopo()
    net = Mininet(topo=topo, controller=lambda name: RemoteController(name, defaultIP='127.0.0.1'), listenPort=6653)
    net.start()

    print
    "Dumping host connections"
    dumpNodeConnections(net.hosts)

    # habilita broadcast
    for host in net.hosts:
        host.cmd('sudo echo 0 > /proc/sys/net/ipv4/icmp_echo_ignore_broadcasts')
    
    CLI(net)
    net.stop()

if __name__ == '__main__':

    print "Usage: smurf_topo <number of nodes>\n"

    setLogLevel('info')
    simpleTest()

