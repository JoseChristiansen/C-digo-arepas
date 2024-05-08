año = int(input("Ingrese un año entre 1900 y 2199:  "))
list = list(range(1901, año+1))
total = 0 

if año > 2199: 
    print("El año ingresado es mayor a 2199, ingrese un numero valido")
    quit()

elif año < 1900:
    print("El año ingresado es menor a 1900, ingrese un numero valido")
    quit()

# A partir de aca es el programa con uso de ciclos (se tiene que descomentar y comentar la otra parte del programa para que funcione)

# else:
#     for i in list:
#         if i % 4 == 0 and i % 100 == 0:
#             total += 0
#         elif i % 4 == 0:
#             total += 1

# print(f"Hay {total} años bisiestos entre {año} y 1900")



# A partir de aca es el programa sin el uso de ciclos (se tiene que descomentar y comentar la otra parte del programa para que funcione)
else: 
    bisiesto = año - 1900
    bisiesto = bisiesto // 4

print(f"Hay {bisiesto} años bisiestos entre {año} y 1900")




    

