import random

# Se importó la libreria "randon"

import interfaz

# Se importó la librería "interfaz"




def  leer_palabra_secreta(palabras):
    palabra_secreta = random.choice(palabras)
    return palabra_secreta

def  pedir_letra(letras_usadas):
        ingreso_letra = " "
        filtro_letra = " "
        letreros = ["z", "y", "x", "w", "v", "u", "t", "s", "r", "q", "p", "o", "ñ", "n", "m", "l", "k", "j", "i", "h", "g", "f", "e", "d", "c", "b", "a"] 
        while True:
        
            ingreso_letra  = str(input("Ingrese sólo una letra\n"))
            filtro_letra = ingreso_letra.lower()
            if filtro_letra in letreros and len(filtro_letra) == 1:
                if filtro_letra not in letras_usadas:
                    ingreso_letra  = filtro_letra
                    if  ingreso_letra   in letras_usadas: #and len(letra) == 1:  # La segunda condicion asegura al programa que aceptará por teclado sólo una letra
                        print(f"La lettra {ingreso_letra } YA EXISTE \n")
                    letras_usadas.append(ingreso_letra )
                    return ingreso_letra 
            
def  verificar_letra(ingreso_letra, palabra_secreta):
    if ingreso_letra in palabra_secreta:
        return True
    else:
        return False
    
def  validar_palabra(letras_usadas, palabra_secreta):
    acum_palabra_secreta = 0
    while True:  
        for i in range(len(palabra_secreta)):    
            if palabra_secreta[i] in letras_usadas:
                acum_palabra_secreta += 1


                # "acum_palabra_secreta"  Acumula el numero de iteraciones a "palabra_secreta"

                if i == acum_palabra_secreta or acum_palabra_secreta == len(palabra_secreta):
                    return True
                    break
            else:
                print("Aun no se ha adivinado la palabra secreta")
                return False
            

if __name__ == "__main__":

    #Bloque principal del programa
    print("\n¡Aquí comienza el juego del ahorcado!\n")
    # Inicializo las variables y listas a utilizar.
    max_cantidad_intentos = 7
    intentos = 0
    letras_usadas = []
    es_ganador = False

    # Leer la palabra secreta de una lista.
    palabras = ["listas", "bucles", "variables"]
    palabra_secreta = leer_palabra_secreta(palabras)
    
    # Esto se realiza para que el jugador pueda ver al principio
    # la cantidad de letras de la palabra a adivinar.
    interfaz.dibujar(palabra_secreta, letras_usadas, intentos)
    
    while intentos < max_cantidad_intentos and not es_ganador:
        # Pedir una nueva letra
        letra = pedir_letra(letras_usadas)

        # Verificar si la letra es parte de la palabra secreta        
        if verificar_letra(letra, palabra_secreta) == False:
            # En caso de no estar la letra ingresada en la palabra
            # a adivinar incremento en 1 la variable intentos.
            intentos += 1
        
        # Dibujar la interfaz
        interfaz.dibujar(palabra_secreta, letras_usadas, intentos)

        # Validar si la palabra secreta se ha adivinado
        if validar_palabra(letras_usadas, palabra_secreta) == True:
            es_ganador = True
            break

    if es_ganador:
        print(f'\n¡Usted ha ganado la partida!, palabra secreta {palabra_secreta}!\n')
    else:
        print('\n¡Ahorcado!')
        print(f'\n¡Usted ha perdido la partida!, palabra secreta {palabra_secreta}!\n')