# 01_rabbitmq_rpc

## FINISHED

Note: this small project is finished. For the time being, no additional functionality is planned. The description below illustrates what this project is about in detail, but as of the moment of completion, the project includes:
- A simple C++ .so library that contains two exported functions.
- A Python server script that listens for a request on a RabbitMQ queue, gets the request, calls the corresponding C++ function from the .so mentioned above, and sends the response back to the client.
- A Python client script that sends a request like "2 + 3" or "33 * 46" to the server, receives a response from it and prints it out on console.

## Description

This is a short-term project the main purpose of which is research and experimentation.

The main idea is as follows. There is a mechanism by which message brokers and remote procedure call / remote method invocation services are able to call functions from a .dll/.so (for example, a dynamic library containing some public C/C++ functions) remotely, that is, from a different machine. This is a test project to research this mechanism specifically in RabbitMQ, and try to successfully implement the PoC/MVP version of a .so with 2-3 functions, and a RabbitMQ adapter that would serve those two functions remotely.

Should contain the following parts:
1. A C++/CMake project with the .so/.dll to call functions from. This can be Linux-only, as it is being developed and is going to be deployed on Arch Linux.
2. A Python wrapper that would wrap the .so calls to those functions, process the remote requests to RabbitMQ, call the functions and send the result to the caller. This can be Linux-only, as it is being developed and is going to be deployed on Arch Linux.
3. Some kind of a client application that would be able to send appropriate requests to the wrapper/server/RabbitMQ. This has to be cross-platform, as this will have to be called on both Arch Linux and Windows 10.

## Licensing

This project is licensed under The Unlicense. This means it is public domain and you can do whatever you want with it without owing me anything.