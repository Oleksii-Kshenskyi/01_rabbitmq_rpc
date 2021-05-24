#!/usr/bin/env python

import pika
import sys
import os
import pathlib
import ctypes

cpp_sopath = pathlib.Path().absolute() / "libsofuncs.so"

def add_two_cpp(one, two):
    cpp_so = ctypes.CDLL(cpp_sopath)
    cpp_so.sum_ints.restype = ctypes.c_ulonglong
    return cpp_so.sum_ints(one, two)

def mul_two_cpp(one, two):
    cpp_so = ctypes.CDLL(cpp_sopath)
    cpp_so.mul_ints.restype = ctypes.c_ulonglong
    return cpp_so.mul_ints(one, two)

def prepare_request_from_bytes(bodybytes):
    bodystr = str(bodybytes, "utf-8")
    bodylist = list(filter(None, bodystr.split(" ")))
    return bodylist

def on_request(ch, method, props, body):
    print("!!! GOT REQUEST: {0}".format(str(body, "utf-8")))
    # translating request for server to understand
    request = prepare_request_from_bytes(body)

    # calculating response
    # error handling
    response = ''
    if (len(request) != 3 or (request[1] != '*' and request[1] != '+')):
        response = 'NOPE'
    try:
        request[0] = int(request[0])
        request[2] = int(request[2])
    except ValueError:
        response = 'NOPE'
    # actual response generation
    if response != 'NOPE':
        if request[1] == '*':
            response = str(mul_two_cpp(request[0], request[2]))
        elif request[1] == '+':
            response = str(add_two_cpp(request[0], request[2]))

    print(f"!!! RESPONSE IS {response}, sending...")
    # sending the response back to client
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=response)
    ch.basic_ack(delivery_tag=method.delivery_tag)


def main():
    if(len(sys.argv) < 2):
        print("NOPE")
        os._exit(1)
    host = sys.argv[1]
    connection = pika.BlockingConnection(pika.ConnectionParameters(host))
    channel = connection.channel()

    channel.queue_declare('rpcdemo')

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='rpcdemo',
                          on_message_callback=on_request)
    print("Waiting for new RPC requests... Press [Ctrl + C] to exit.")
    channel.start_consuming()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("[Ctrl + C] pressed, exiting...")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)