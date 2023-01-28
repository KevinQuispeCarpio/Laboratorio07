from collections import Counter
def conta(palabra):
    conta = Counter(palabra)
    repeticiones = [t[1] for t in list(conta.items()) if t[1] > 1]
    return len(repeticiones)

def tamaño(cadena):
    lista = cadena.split()
    print(lista)
    for i in lista:
        if conta(i) == 0:
            return "tamaño de cadena :  "+ str(len(i)) + " valor de cadena : "+ str(i)

print(tamaño("Estructura de Datos"))
    