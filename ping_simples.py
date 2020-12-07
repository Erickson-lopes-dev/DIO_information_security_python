import os

ip_ou_host = input("Digite o IP ou host a ser verificado: ")

os.system(f'ping -n 6 {ip_ou_host}')

