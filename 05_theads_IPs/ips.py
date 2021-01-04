import ipaddress

# ip = '192.168.0.1'
#
# endereco = ipaddress.ip_address(ip)

ip = '192.168.0.0/4'

rede = ipaddress.ip_network(ip, strict=False)

# imprimir todos os ip
for ip in rede:
    print(ip)
else:
    print()
print(rede)
