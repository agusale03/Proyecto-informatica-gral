
def validar_ingreso_denumero():

    mensajeInput ="Ingrese un numero mayor que 0 "
    datoParaDevolver = None
    while datoParaDevolver == None:
        try:
            numero = int(input(mensajeInput))#Si el usuario pone "pepe", se lanza excepcion, pero como estoy en 
            #si int no lanzo excepcion (ValueError) entonces el usuario puso un numero, pero sera el que queriamos?, hay que chequear eso tambien
            if numero <= 0:
                mensajeInput = "Usted ha ingresado un numero, pero no es mayor que 0, por favor ingrese un numero > 0 "
            else:
                datoParaDevolver = numero
        except ValueError:
            #este codigo se corre si el codigo de arriba (el de adentro del try, lanza excepcion)
            mensajeInput = "Usted no ingreso un numero, por favor ingrese un numero mayor que 0 "
    
    return datoParaDevolver

def validar_ingreso_menu():

    mensajeInput ="Ingrese un numero mayor que 0 "
    datoParaDevolver = None
    while datoParaDevolver == None:
        try:
            numero = int(input(mensajeInput))#Si el usuario pone "pepe", se lanza excepcion, pero como estoy en 
            #si int no lanzo excepcion (ValueError) entonces el usuario puso un numero, pero sera el que queriamos?, hay que chequear eso tambien
            if numero <= 0 or numero > 5:
                mensajeInput = "Usted ha ingresado un numero, pero no es mayor que 0, por favor ingrese un numero > 0 "
            else:
                datoParaDevolver = numero
        except ValueError:
            #este codigo se corre si el codigo de arriba (el de adentro del try, lanza excepcion)
            mensajeInput = "Usted no ingreso un numero, por favor ingrese un numero mayor que 0 "
    
    return datoParaDevolver

def sacar_comillas(cadena):
    for letra in cadena:
        if letra == "'":
            letra = ""
        else:
            return letra
    return cadena

print(sacar_comillas('"Hola soy Fran'))
    
def transformacion_de_numeros_a_int(lista):
    i = 0
    while i < len(lista):
        try:
            lista[i] = int(lista[i])
            i += 1
        except ValueError:
            i += 1
    return lista


    


locales = [["'sol'",'sos','muy','crack'],[],[],[]]
    
print (sacar_comillas(locales[0][0]))





""" 1.	CALLE: Se considera tipo String. Al guardar como dato separado, sacarle las comillas dobles si las tuviera.
2.	SUPERFICIE: Se considera tipo int. 
3.	PRECIOUSD: Se considera tipo int. 
4.	PRECIOPESOS: Se considera tipo int. 
5.	USDM2: Se considera tipo int. 
6.	ANTIG: Se considera tipo int. Si es a estrenar, vale 0.
7.	EN_GALERIA: Se considera tipo String. Puede valer únicamente SI o NO, o bien estar vacío (no se tiene el dato)
8.	COTIZ: Se considera tipo int.
9.	TRIMESTRE: Se considera tipo String Puede valer únicamente PRIMER, SEGUNDO, TERCER o CUARTO.
10.	BARRIO: Se considera tipo String
11.	COMUNA: Se considera tipo int. Son números del 1 al 15. """

