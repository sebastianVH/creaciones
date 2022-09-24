import os #importacion de clean screen 
import ascii #evitamos errores de caracteres

def inicio():
    clave=[]
    espacio=[]
    usadas=[]
    test_letras=False
    while test_letras==False:
        datos=input('Ingrese palabra a adivinar: ')
        if datos.isalpha():
            test_letras=True
        else:
            print('La palabra ingresada contiene caracteres invalidos (numeros o espacios)')
    datos=datos.lower()    
    os.system('cls')
    #creo una lista llamada "clave" con cada letra y una lista con espacios, por cada letra
    for i in datos:
        clave.append(i)
        espacio.append("_")
    print(f"Adivinemos la palabra! Su largo es de {len(clave)} casilleros\n")
    for i in espacio:
        print(i,end=' ')
    print('\n')
    return usadas,datos,clave,espacio

def elegir_letra(intentos):
    test_letras=False
    while test_letras==False:
        letra = input("Elija una letra: ") #pedimos una letra, y usamos este for para recorrer la lista clave y ver si esta la letra.
        if letra.isalpha():
            test_letras=True
        else:
            print('Se ingresó un caracter inválido')
    letra=letra.lower()
    contador = 0
    usadas.append(letra.upper())
    for x in range(len(clave)):
        if letra == clave[x]: #si encontramos una coincidencia, pegamos esa letra en la misma posicion de la lista espacio
            espacio[x]=letra.upper()
            contador = contador+1
    if contador == 0:
        intentos = intentos-1
        if intentos == 0:
            print(f'GAME OVER! Te quedaste sin intentos! La palabra era {datos.upper()}')
            return intentos
        else:
            print(f'No acertaste la letra! te quedan {intentos} intentos')
    for i in espacio:
        print(i,end=' ')
    print('\n')
    return intentos    

def arriesgar_palabra(intentos):
    test_letras=False
    while test_letras==False:
        adivina=input("Introduzca la palabra: ")
        if adivina.isalpha():
            test_letras=True
        else:
            print('La palabra ingresada contiene caracteres invalidos (numeros o espacios)')
    adivina=adivina.lower()
    if adivina==datos:
         print(f"Acertaste!! La palabra era {datos.upper()}\nGracias por jugar!!")
         intentos=0
         return intentos
    else:
        intentos=intentos-1
        if intentos > 0:
            print(f"No es la palabra correcta! Te quedan {intentos} intentos \n")
            return intentos
        elif intentos==0:
            print(f'GAME OVER! Te quedaste sin intentos! La palabra era {datos.upper()}')
            return intentos

def juego():
    adivina=None
    intentos=7
    while datos != adivina and intentos !=0: #este while sirve para realizar el juego, hasta que la palabra se adivine o se acaben los intentos
        seleccion=input("Elija una opcion:\n1) Elegir Letra\n2) Arriesgar palabra\n3) Ver lista de letras usadas\n")
        if seleccion == '1':
            intentos=elegir_letra(intentos)
        elif seleccion =='2':
            intentos=arriesgar_palabra(intentos)
        elif seleccion=='3':
                for i in usadas:
                    print(i,end='-')
                print('\n')
        else:
            print('Opcion elegida no valida\n')
      
usadas,datos,clave,espacio=inicio()
juego()