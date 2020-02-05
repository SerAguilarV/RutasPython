# Leer carpeta por niveles

import os

levels = int(input("Choose the amount of level you can see: \n"))
inicio = "C:\\"
Carpetas = []
Documentos = []
RutaSig = [inicio]
rutasV = []

for i in range(levels):
    RutasSig = []
    for pth in RutaSig:
        try:
            Carpetas = [i for i in os.listdir(pth) if not "." in i]
            Documentos = [i for i in os.listdir(pth) if "." in i]
            if Carpetas == [] and Documentos == []:
                rutasV.append(pth) 
                # print("Ruta Vacia: {}".format(pth))
            RutasSig += [pth + i + "\\" for i in Carpetas]
        except:
            pass
    RutaSig = RutasSig 

for i in rutasV:
    if not  os.path.expanduser("~")  in i:
        rutasV.remove(i)
    else:
        print(i)

