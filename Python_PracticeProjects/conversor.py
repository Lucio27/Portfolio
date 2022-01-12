def conversor(tipo_pesos, valor_dolar):
    pesos = input("Ingresa la cantidad de pesos " + tipo_pesos + " que quieras convertir: ")
    pesos= float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2) #Estamos redondeando a dos decimales
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")

menu = """"
Bienvenido al conversor de monedas 😁

1.- Pesos mexicanos
2.- Pesos argentinos
3.- Pesos colombianos

Elige una opcion: """
opcion = int(input(menu))

if opcion == 1:
    conversor("colombianos", 3875)
elif opcion == 2:
    conversor("argentinos", 65)
elif opcion == 3:
    conversor("mexicanos", 24)
else:
    print("Ingresa una opcion correcta porfavor")




