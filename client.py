import socket
Host="localhost"
Port=12457

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((Host,Port))
while s:
    mensagem = input("diga sua mensagem")
    s.send(str.encode(mensagem))
    dados=s.recv(1024)
    print("mensagem enviada: ",dados.decode())

    if(dados=="sair"):
        print("Conexao encerrada")
    s.close()
    break