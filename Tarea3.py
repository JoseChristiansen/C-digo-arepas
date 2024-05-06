genero = input("""Elige una opcion:
               1. Niño
               2. Niña
               3. Adulto
               
               => """)

welcome = "Bienvenid"

if genero == "3":
    welcome = "Esto es un juego para niños"
    print(welcome)
    quit()

edad = int(input("Que edad tienes??: "))

if edad <= 10:
    if genero == "1":
        welcome = "Eres muy menor para ser entrenador"
    elif genero == "2":
        welcome = "Eres muy menor para ser entrenadora"
    print(welcome)
    quit()
elif edad > 10:
    if genero == "1":
        welcome += "o"
        genero = "Niño"
    elif genero == "2":
        welcome += "a"
        genero = "Niña"
    else:
        print("debe elegir una opcion valida, vuelva a correr el programa")
        quit()
    print(welcome)



region = input("""De que region eres??: 
               1. Caracas
               2. Bogota
               3. Santiago de Chile
               
               
            =>  """)

if region == "1":
    region = "Caracas"
elif region == "2":
    region = "Bogota"
elif region == "3":
    region = "Santiago de Chile"
else: 
    print("Debe elegir una opcion valida, vuelva a correr el programa")
    quit()

pokemon = input("""Cual es tu pokemon favorito??: 
               1. Bulbasaur
               2. Charmander
               3. Squirtle
                
                =>  """)
if pokemon == "1":
    pokemon = "Bulbasaur"
elif pokemon == "2":
    pokemon = "Charmander"
elif pokemon == "3":
    pokemon = "Squirtle"
else: 
    print("Debe elegir una opcion valida, vuelva a correr el programa")
    quit()


print(f"""Tu perfil de entrenador es:
      Genero = {genero}
      Region: {region}
      Pokemon favorito: {pokemon}""")




