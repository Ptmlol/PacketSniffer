# PacketSniffer
Linux Python3 program used to sniff packets from unsecure HTTP websites, at the moment it sniffes usernames and passwords entered while the target is being ARP spoofed.
Windows/Python<3/HTTPS coming soon..

You can change what is sniffes modifying the contents of the "keywords" list with anything you want to be sniffed.
Wait for futher edits on this repo to make it work on HTTPS too and other information besides username/passwords. It also tracks protocols used(TCP/UDP).
Use >python3 packetsniffer.py --help   in the Linux terminal to display the syntax and other useful information.
It sniffes the selected interface in the --target argument. Works well with ARP Spoofer program.
