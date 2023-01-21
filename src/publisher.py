#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" 
Publish some messages to queue
"""
import paho.mqtt.publish as publish
import msgpack


msgs = [{'topic': "kids/yolo", 'payload': "jump"},
        {'topic': "adult/pics", 'payload': "some photo"},
        {'topic': "adult/news", 'payload': "extra extra"},
        {'topic': "adult/news", 'payload': "super extra"}]

host = "localhost"


if __name__ == '__main__':
    # publish a single message

    msg = bytearray(msgpack.packb({'data': False}))
    publish.single(topic="ping", payload=msg, hostname=host)

    # msg = bytearray(msgpack.dumps({'data': "Hello"}))
    # publish.single(topic="echo", payload=msg, hostname=host)


    # publish multiple messages
    # publish.multiple(msgs, hostname=host)


# vi: set fileencoding=utf-8 :
