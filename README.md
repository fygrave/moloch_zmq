
moloch_zmq
==========



This ZMQ integration/data explort plugin for Moloch (http://github.com/aol/moloch/). The current implementation
Acts as ZMQ PUB(lisher), which you need to connect to using your client(s) and perform additional real-time analysis
of network data. 

Presently only HTTP traffic (src ip, dst ip, ports, url and X-Forwarded-For headers are sent). The plugin could be further 
extended to hook into other protocols as well.

Only two 0MQ patterns are supported on the moment. Push/Pull and Pub/Sub. 


Requirements:
============
0MQ 3.x or later.

    add-apt-repository ppa:chris-lea/zeromq
    apt-get update
    apt-get install libzmq3-dev

Installation:
=============

Move zmqexp.c, Makefile.in (and Makefile) into capture/plugins/ folder. Compile as you'd regularly compile your moloch.

Running:
=======
add content of config.ini to your default section of moloch's config.ini. Feel free to modify ZMQ binding string as you find suitable.
Sample client in python is provided.

