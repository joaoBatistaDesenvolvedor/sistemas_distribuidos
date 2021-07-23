
import socket                               # Import socket module

s = socket.socket()                         # Create a socket object
host = socket.gethostname()                 # Get local machine name
port = 12345                                # Reserve a port for your service.
s.bind((host, port))                        # Bind to the port

s.listen(5)                                 # Now wait for client connections.
print("aguardando conexao")
while True:
   c, addr = s.accept()
   print('usuario conectado ', addr)
   print("MENSAGEM RECEBIDO".encode())
   c.close()