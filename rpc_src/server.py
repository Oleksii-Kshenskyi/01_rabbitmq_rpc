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

def main():
    def callback(ch, method, properties, body):
        print("!!! RECEIVED: [{0}]".format(str(body, "utf-8")))

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare('rpcdemo')

    channel.basic_consume(auto_ack=True,
                        queue='rpcdemo',
                        on_message_callback=callback)
    print("Waiting to receive messages from the 'rpcdemo' queue... Press [Ctrl + C] to exit.")
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