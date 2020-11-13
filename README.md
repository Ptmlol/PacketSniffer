# PacketSniffer
Linux program used to sniff packets from unsecure HTTP websites, at the moment it sniffes usernames and passwords entered while the target is being ARP spoofed.
Windows/HTTPS coming soon..

You can change what is sniffes modifying the contents of the "keywords" list with anything you want to be sniffed.
Wait for futher edits on this repo to make it work on HTTPS too and other information besides username/passwords. It also tracks HTTP Requests.
Use:
#>python packetsniffer.py --help   in the Linux terminal to display the syntax and other useful information.

It sniffes the selected interface in the --target argument. Works well with ARP Spoofer program but remember to enable iptables queue:

_#iptables -I FORWARD -j NFQUEUE --queue-num 0_
and portforrwarding if you want to test it on a different computer 
_#echo 1 > /proc/sys/net/ipv4/ip_forward_

Use in this order instead of the "FORWARD" iptables command:

_#> iptables -I INPUT -j NFQUEUE --queue-num 0_    without the # in the linux terminal and
_#> iptables -I OUTPUT -j NFQUEUE --queue-num 0_ in the linux terminal if you want to test it on your own computer.
