def DiccionarioT(texto):
    retiro = ".;:.\n\"'"
    for i in retiro:
        texto = texto.replace(i,"")
    texto.lower()
    list_palabras = texto.split(" ")
    diccionario = {}
    for i in list_palabras:
        if i in diccionario:
            diccionario[i] += 1
        else:
            diccionario[i] = 1
    for j in diccionario:
        cantidad = diccionario[j]
        print(f"Palabra {j} se repite {cantidad}")
DiccionarioT("Una tortura a otra tortuga a otra tortuga tuerta que tropieza con la tuerca tras la puerta")