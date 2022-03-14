

num = int (input("ingrese un numero: ") )


resultado = 0


print(resultado)

def myFuncion(parametro1, parametro2):
    if(parametro1 > 0):
        resultado = parametro1**parametro2
        hola = "hola"
        print("dentro de la funcion")
        print(resultado)
    else:
        resultado = parametro1 + parametro2
        print(resultado)

    return resultado

# for numero in range(3):
#     print("dentro del for")
#     print(numero)
#     num = int (input("ingrese un numero: ") )
#     resultado2 = myFuncion(num, 2)
#     print(resultado2)


lista = []
lista2 = [ "edwing", 3, "edu" ]

lista2.append("teban")



# print(lista2[0])
# print(lista2[1])
# print(lista2[2])
# print(lista2[3])

tamanio = len(lista2)

for posicion in range(tamanio):
    print (lista2[posicion])
