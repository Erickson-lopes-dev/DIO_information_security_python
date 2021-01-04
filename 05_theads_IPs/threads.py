import time
from threading import Thread


def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        trajeto += velocidade
        time.sleep(0.5)
        print(f'Carro: {velocidade}km ({piloto})\n')


t_carro1 = Thread(target=carro, args=[10, 'Python'])

t_carro2 = Thread(target=carro, args=[25, 'Senna'])

t_carro1.start()
t_carro2.start()
