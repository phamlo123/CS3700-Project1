import socket

studentID = '001418312'
host = 'proj1.3700.network'
port_number = 27993
my_socket = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect ((host, int (port_number)))

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
        ls = portion.decode().split(' ')

        print (ls[2])
        exit ()
    else:
        print('Wrong message type')
        exit()


hello_message = 'ex_string HELLO ' + studentID + '\n'
my_socket.sendall (bytes (hello_message, 'utf-8'))
executeThisCodes ()
