import hashlib

arquivo1 = 'a.txt'
arquivo2 = 'b.txt'


# Construtor / algoritmo de hash(ripemd de 160 bits)
hash1 = hashlib.new('ripemd160')

# dado a ser comparado(no caso arquivo(leitura mobo binario))
hash1.update(open(arquivo1, 'rb').read())

# repetindo o processo
hash2 = hashlib.new('ripemd160')
hash2.update(open(arquivo2, 'rb').read())


# fazer comparação (resultado passado peçp update resumido peço digest() )
if hash1.digest() != hash2.digest():
    print('Os hash são diferentes!')
    print(f'O arquivo {arquivo1} é diferente do {arquivo2}\n')

    print(f'{arquivo1} = {hash1.hexdigest()}')
    print(f'{arquivo2} = {hash2.hexdigest()} \n')
else:
    print('Os hash são iguais')
    print(f'O Arquivo {arquivo1} é Igual do {arquivo2} \n')

    print(f'{arquivo1} = {hash1.hexdigest()}')
    print(f'{arquivo2} = {hash2.hexdigest()} \n')

print(hash1.digest())
print(hash2.digest())
