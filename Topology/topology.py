#!/usr/bin/python

import os
from mininet.net import Mininet
from mininet.node import RemoteController, OVSSwitch
from mininet.link import TCLink
from mininet.link import Intf
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def emptyNet():
    net = Mininet( topo=None, build=False )
    info( '*** Adding controller\n' )
    net.addController('c0',controller=RemoteController, ip="117.16.136.102",port=6653)
    info( '*** Adding hosts\n' )
    h1 = net.addHost('h1', ip='10.0.1.5')
    h2 = net.addHost('h2', ip='10.0.1.6')
    h3 = net.addHost('h3', ip='10.0.2.5')
    h4 = net.addHost('h4', ip='10.0.2.6')

    info( '*** Adding switch\n' )
    s1 = net.addSwitch( 's1', cls=OVSSwitch )
    s2 = net.addSwitch( 's2', cls=OVSSwitch )
    s3 = net.addSwitch( 's3', cls=OVSSwitch )
    s4 = net.addSwitch( 's4', cls=OVSSwitch ) # top
    s5 = net.addSwitch( 's5', cls=OVSSwitch ) # center
    s6 = net.addSwitch( 's6', cls=OVSSwitch )
    s7 = net.addSwitch( 's7', cls=OVSSwitch )
    s8 = net.addSwitch( 's8', cls=OVSSwitch )

    info('*** Creating links\n')
    ## host - switch
    net.addLink( h1, s1,cls=TCLink,bw=1000,delay='1ms',loss=0)
    net.addLink( h2, s1,cls=TCLink,bw=1000,delay='1ms',loss=0)
    net.addLink( h3, s6)
    net.addLink( h4, s6)

    ## switches
    # s1
    net.addLink(s1, s2)
    net.addLink(s1, s5)
    net.addLink(s1, s3)
    # s2
    net.addLink(s2, s4)
    net.addLink(s2, s5)
    # s3
    net.addLink(s3, s5)
    net.addLink(s3, s8)
    # s4
    net.addLink(s4, s5)
    net.addLink(s4, s7)
    # s6
    net.addLink(s6, s7)
    net.addLink(s6, s5)
    net.addLink(s6, s8)
    # s7
    net.addLink(s7, s5)
    # s8
    net.addLink(s8, s5)

    info( '*** Starting network\n')
    net.start()
      
    os.popen ('ovs-vsctl add-port s1 eth0')
    h1.cmdPrint('dhclient '+h1.defaultIntf().name)
    h2.cmdPrint('dhclient '+h2.defaultIntf().name)

    #info('*** Set ip address to switch\n')
    s1.cmd('ifconfig s1 10.0.1.1')
    s2.cmd('ifconfig s2 10.0.1.2')
    s3.cmd('ifconfig s3 10.0.1.3')

    s4.cmd('ifconfig s4 10.0.3.2')
    s5.cmd('ifconfig s5 10.0.3.1')

    s6.cmd('ifconfig s6 10.0.2.1')
    s7.cmd('ifconfig s7 10.0.2.2')
    s8.cmd('ifconfig s8 10.0.2.3')

    info( '*** Running CLI\n' )
    CLI(net)

    info( '*** Stopping network' )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()
