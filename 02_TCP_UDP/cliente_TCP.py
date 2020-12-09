import socket
import sys


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print('Erro na conexão!')
        print(f'Erro: {e}')
        sys.exit()
    else:
        print('Socket criado com sucesso!')

    host_alvo = input('Digite o Host ou Ip a ser conectado: ')
    posta_alvo = input('Digite a porta a ser conectada: ')

    try:
        s.connect((host_alvo, int(posta_alvo)))
    except socket.error as err:
        print(f'Erro: {err}')
    else:
        print(f'Cliente TCP conectado com sucesso! no host {host_alvo}')
        s.shutdown(2)
        sys.exit()


if __name__ == '__main__':
    main()
