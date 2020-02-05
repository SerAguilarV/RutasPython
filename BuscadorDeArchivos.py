# Leer carpeta por niveles

import os

#levels = int(input("Choose the amount of level you can see: \n"))
inicio = "C:\\"
Carpetas = []
Documentos = []
RutaSig = [inicio]
flag = False

mensaje = """Ruta donde fue encontrado: {}

Documentos en la carpeta:
{}

Carpetas:
{}"""

while not flag:
    RutasSig = []
    for pth in RutaSig:
        try:
            Carpetas = [i for i in os.listdir(pth) if not "." in i]
            Documentos = [i for i in os.listdir(pth) if "." in i]
            if "VAL 13 09 2019.xlsx" in Documentos:
                print(mensaje.format(pth, Documentos, Carpetas))
                RutasSig = [pth + i + "\\" for i in Carpetas]
                flag = True
                break

            if not flag:
                RutasSig += [pth + i + "\\" for i in Carpetas]
        except:
            pass
    RutaSig = RutasSig 
