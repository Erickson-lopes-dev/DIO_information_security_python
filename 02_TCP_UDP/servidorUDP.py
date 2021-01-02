import socket

# chama o método socket(protocolo ip, tipo de conexao)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# se foi criado com sucesso

print('Socket criado com sucesso')

host = 'localhost'

port = 5432
# faz a ligacao do host e porta
s.bind((host, port))

# mansagem pro client
mensagem = '\nSevidor: Olá cliente '

while True:
    # dados / endereço com 4096 bits
    dados, end = s.recvfrom(4096)

    # se tiver dados
    if dados:
        print('\nServidor: enviando mensagem... ')
        # envia mensagem
        s.sendto(dados + (mensagem.encode()), end)
