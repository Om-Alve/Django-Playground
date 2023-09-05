from socket import *

def create_server():
    sock = socket(AF_INET,SOCK_STREAM)
    try:
        sock.bind(('localhost',9000))
        while True:
            sock.listen(5)

            (clientsocket,address) = sock.accept()

            rd = clientsocket.recv(5000).decode()

            pieces = rd.split('\n')

            if len(pieces) > 0 : print(pieces[0])
    
            data = "HTTP/1.0 200 OK\r\n"

            data+= "Content-type: Text/HTML\r\n"

            data+= "\r\n"

            data+= "<html><body><h1>Hello world</h1><body></html>\r\n\r\n"

            clientsocket.sendall(data.encode())

            clientsocket.shutdown(SHUT_WR)
    except KeyboardInterrupt:
        print("Shutting down....\n\n")
    except Exception as exc:
        print("Error:")
        print(exc)

    sock.close()

print("Access http://localhost:9000")
create_server()





        
