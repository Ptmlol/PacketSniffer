# PacketSniffer
Program used to sniff packets from unsecure HTTP websites, at the moment it sniffes usernames and passwords entered while the target is being ARP spoofed.
Windows/Linux compatible. Check for interpreter and libraries.

Use sslstrip to make it work for certain HTTPS websites.

You can change what is sniffes modifying the contents of the "keywords" list with anything you want to be sniffed.
Wait for futher edits on this repo to make it work on HTTPS too and other information besides username/passwords. It also tracks HTTP Requests.
Use:
>python packetsniffer.py --help   in the Linux terminal to display the syntax and other useful information.

It sniffes the selected interface in the --target argument. Works well with ARP Spoofer program but remember to enable iptables queue:


> iptables -I FORWARD -j NFQUEUE --queue-num 0 and portforrwarding if you want to test it on a different computer 


> echo 1 > /proc/sys/net/ipv4/ip_forward

Use in this order instead of the "FORWARD" iptables command:

> iptables -I INPUT -j NFQUEUE --queue-num 0   without the # in the linux terminal and


> iptables -I OUTPUT -j NFQUEUE --queue-num 0 in the linux terminal if you want to test it on your own computer.
