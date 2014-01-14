#!/usr/bin/env python

import zmq
context = zmq.Context()
socket = context.socket(zmq.PULL)
socket.connect("tcp://127.0.0.1:3240")


while True:
    d = socket.recv()
    rez = d.split("\t")
    print rez
    print len(rez)
