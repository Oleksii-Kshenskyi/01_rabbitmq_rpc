#!/usr/bin/env python

import pika
import sys
import os
import uuid
corr_id = str(uuid.uuid4())
response = ''
def on_response(ch, method, props, body):
    if corr_id == props.correlation_id:
        globals()['response'] = str(body, "utf-8")
        print(f"!!! GOT RESPONSE: {response}")


# establishing connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

result = channel.queue_declare('', exclusive=True)
callback_queue = result.method.queue

channel.basic_consume(auto_ack=True,
                      queue=callback_queue,
                      on_message_callback=on_response)

# preparing request from cmdline arguments
if(len(sys.argv) < 4):
    print("NOPE")
    os._exit(1)
num1 = sys.argv[1]
op = sys.argv[2]
num2 = sys.argv[3]
request = " ".join([num1, op, num2])

channel.basic_publish(exchange='',
                      routing_key='rpcdemo',
                      body=request,
                      properties=pika.BasicProperties(
                          reply_to=callback_queue,
                          correlation_id=corr_id
                      ))
print(f"!!! Sent request for {request}, waiting for response!")
while response == '':
    connection.process_data_events()

connection.close()