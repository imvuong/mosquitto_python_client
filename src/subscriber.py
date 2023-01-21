#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A small example subscriber
"""
import paho.mqtt.client as paho
import msgpack
import json

def convert(data):
    if isinstance(data, bytes):  return data.decode()
    if isinstance(data, dict):   return dict(map(convert, data.items()))
    if isinstance(data, tuple):  return tuple(map(convert, data))
    if isinstance(data, list):   return list(map(convert, data))
    return data

def on_message(mosq, obj, msg):
    # print ("%-20s %d %s" % (msg.topic, msg.qos, msg.payload))
    # mosq.publish('pong', 'ack', 0)
    # {b'header': 
    #   {b'seq': 650, 
    #   b'stamp': 
    #       {b'secs': 1671214349, b'nsecs': 23126363}, 
    #   b'frame_id': b''
    # }, 
    # b'name': [b'joint_0', b'joint_1', b'joint_2', b'joint_3', b'joint_4', b'joint_5'], 
    # b'position': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
    # b'velocity': [], 
    # b'effort': []}
    unpacked = msgpack.unpackb(msg.payload)
    new_data = convert(unpacked)
    print(new_data['position'][0])

def on_publish(mosq, obj, mid):
    pass

if __name__ == '__main__':
    client = paho.Client()
    client.on_message = on_message
    client.on_publish = on_publish

    #client.tls_set('root.ca', certfile='c1.crt', keyfile='c1.key')
    client.connect("127.0.0.1", 1883, 60)

    # client.subscribe("kids/yolo", 0)
    # client.subscribe("adult/#", 0)
    client.subscribe("joint_states", 0)

    while client.loop() == 0:
        pass

# vi: set fileencoding=utf-8 :
