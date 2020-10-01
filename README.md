## Welcome to Alpha Port Scanner
**Alpha port scanner** (apscan) is an open source port scanner designed to scan a server or host for open ports. 
Alpha-Port-Scanner is really simple port scanner , for times when we can't use nmap. 

Installation:

Download alpha-port-scanner using command
git clone https://github.com/AlphaQx/Alpha-Port-Scanner.git

then, go to Alpha-port-scanner directory using command:
cd alpha-port-scanner

Now run apscan using command
python apscan.py [ip address] [start point] [end point]
 
example:
To scan all open ports from 1 to 200 of example.com
python apscan.py example.com 1 200

![screenshot](https://user-images.githubusercontent.com/71433469/94832827-07bf9400-042c-11eb-8e06-73b5ae532ced.png)
