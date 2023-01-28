def SUBCADENAL(palabra):
    subcadenas = palabra.split()
    lista_cadenas = []
    for i in subcadenas:
        lista_cadenas.append(len(i))
    for j in subcadenas:
        if len(j) == max(lista_cadenas):
            return str(i) + " de valor : " + str(len(j))

print("Valor de la cadena mas larga : "+SUBCADENAL(
    "pepe pecas pica papas con un pico, con un pico pica papas pepe pecas. Si pepe pecas pica papas con un pico,¿dónde está el pico con que pepe pecas pica papas?"))
