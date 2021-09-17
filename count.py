#!/usr/bin/env python3

import socket
import ssl
import sys

#This function calculates the number of repetitions of the given character and communicate that with the server until
#the BYE message is received or it terminates the program if a message type from the server is not recognized (not one
#of 4 types)

def executeThisCodes ():
    portion = my_socket.recv (8192)

    count = 0
    if portion.decode ().split (' ')[1] == 'FIND':
        ls = portion.decode ().split (' ')
        char = ls[2]
        result = ls[3]
        while True:
            if portion.decode ()[-1] == '\n':
                break
            else:
                portion = my_socket.recv (8192)
                result = result + portion.decode ()
        for element in result:
            if char == element:
                count = count + 1
            else:
                continue

        countMessage = 'ex_string COUNT {}\n'.format (count)

        my_socket.sendall (bytes (countMessage, 'utf-8'))
        executeThisCodes ()

    elif portion.decode ().split (' ')[1] == 'BYE':
        ls = portion.decode ().split (' ')

        print (ls[2])
        exit ()
    else:
        print ('Wrong message type')
        exit ()


host = sys.argv[-2]
studentID = sys.argv[-1]
port_number = 27993

#if user provides -p in the command line. This means the program will look for the given port number
if sys.argv[1] == '-p':
    if len (sys.argv) < 6 and '-s' in sys.argv:
        print ('Error: no port provided')
        exit ()
    elif len (sys.argv) < 5:
        print ('Error: missing input')
        exit ()
    else:
        port_number = sys.argv[2]
#if '-s' is provided in the command line but not port number given then automatically assume it is 27994
elif sys.argv[1] == '-s':
    port_number == 27994

#This create a TCP socket connection with the server since '-s' is not provided
if '-s' not in sys.argv:
    my_socket = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect ((host, int (port_number)))
#If '-s' is provided then make a TLS socket connection
else:
    tempsocket = socket.create_connection ((host, port_number))
    my_socket = ssl.wrap_socket (tempsocket)

#send the Hello message to the server after estabilishing socket connection above and call
# the defined function executeThisCodes() to start the program
hello_message = 'ex_string HELLO ' + studentID + '\n'
my_socket.sendall (bytes (hello_message, 'utf-8'))
executeThisCodes ()
