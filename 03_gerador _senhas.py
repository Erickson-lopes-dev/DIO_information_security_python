import random
import string

tamanho = int(input("Digite o tamanho da senha desejada: "))

# chars = string.ascii_lowercase  SÓ LETRAS MINUSCULAS
# chars = string.ascii_uppercase  SÓ LETRAS MAIUSCULAS

# estrutura da senha gerada / com letras maiu/minu / numeros / caracteres especiais
chars = string.ascii_letters + string.digits + '!@#$%&*(){}?/-=_~´^ç'

# puxa a classe os utilizando a classe urandom / gera numeros aleatórios apartir do sistema
rnd = random.SystemRandom()

# para cada item do loop ele pega um elemento do chars de modo aleatório, gerando 16 caracteres forando a senha
print('Senha aleatória: ', ''.join(rnd.choice(chars) for i in range(tamanho)))

# testes
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
