import ctypes

atributos_ocultar = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW('ocultar', atributos_ocultar)

if retorno:
    print('arquivo foi ocultado')
else:
    print('arquivo não foi ocultado')
