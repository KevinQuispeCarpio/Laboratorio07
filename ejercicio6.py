import re
def reemplazoP(cadena, subcadena, subcadena_cambio):
    return re.sub(subcadena, subcadena_cambio, cadena)


pala = "alegría, alegría llegó el Carnaval dame las caretas ponte el disfraz alegría, alegría estamos en Carnaval toca las maracas sacame a bailar"
subcadena = "alegría"
subcadenaC = "Ayacucho"
print(reemplazoP(pala, subcadena, subcadenaC))