import hashlib

string = input("Digite a string para hash: ")

menu = int(input(''' 
### ESCOLHA O TIPO DE HASH ### 
    1) MD5
    2) SHA1 
    3) SHA256
    4) SHA512
Digite o número do hash a ser gerado: '''))

if menu == 1:
    resultado = hashlib.md5(string.encode())
    print(f'O hash de {string} utilizando o hash MD5 é:', resultado.hexdigest())

elif menu == 2:
    resultado = hashlib.sha1(string.encode())
    print(f'O hash de {string} utilizando o hash sha1 é:', resultado.hexdigest())

elif menu == 3:
    resultado = hashlib.sha256(string.encode())
    print(f'O hash de {string} utilizando o hash sha256 é:', resultado.hexdigest())

elif menu == 4:
    resultado = hashlib.sha512(string.encode())
    print(f'O hash de {string} utilizando o hash sha512 é:', resultado.hexdigest())

else:
    print("Digite apenas as opções do menu.")
