import os

with open("hosts") as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        os.system(f'ping -n 2 {ip}')
