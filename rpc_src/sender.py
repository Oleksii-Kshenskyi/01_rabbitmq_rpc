#!/usr/bin/env python

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare('rpcdemo')

channel.basic_publish(exchange='',
                      routing_key='rpcdemo',
                      body='OMG DOES IT ACTUALLY WROK?!')
print("!!! Sent a message to the 'rpcdemo' queue!")

connection.close()