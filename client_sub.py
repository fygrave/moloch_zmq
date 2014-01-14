#!/usr/bin/env python

import zmq
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://127.0.0.1:3240")
socket.setsockopt(zmq.SUBSCRIBE, "http")

while True:
    d = socket.recv()
    rez = d.split("\t")
    print rez
    print len(rez)
