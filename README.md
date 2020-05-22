# Network_Automation_SITE_1
My first GNS3 Topology configured and automated using Ansible &amp; Python.

OVERVIEW:

The goal of this site is to do configure a simple network (2 routers, 1 switch) with Ansible. Once the topology is up and all 
network devices can reach the internet, i will create python scripts using the netmiko library to automate daily tasks, and 
make changes to network devices. 

HARDWARE & SOFTWARE:

I am currently running ubuntu 18.04 client as my desktop OS (operating system), this is the hypervisor for the emulated network
devices running in GNS3. I am using Cisco VIRL images for the 2 routers and 1 switch in this topology. All code implemented was
edited and created using VSCODE. All code will be executed from my desktop terminal. The emulated network devices connect to a
GNS3 NAT cloud internet appliance, this allows them to access the internet.

NETWORK PROTOCOLS:

The NAT cloud hosts a DHCP pool and is the gateway to the internet.
VIRLR1(router 1) - Static route, OSPF, NTP, DNS, SCP, SNMP
VIRLR2(router 2) - OSPF, NTP, DNS, SCP, DHCP, SNMP
IOSvL2_S1(switch1) - DHCP Snooping, ARP Inspection, VLANS, Port Security, SNMP, SVIs

NETWORK DIAGRAM:
All network diagrams will be created using an open-sourced version of Microsoft Visio.

SUMMARY:
This project is too improve my skills with automating Cisco networks and using GIT as version control for my nodes. 
