def verificar_victoria(tablero): ###Funcion que verifica si haz logrado ganar la parida, o aun no
    x=0
    for fila in tablero:
        for dato in fila:
            if(dato==-1): ###Realiza una comparacion a cada valor dentro del tablero, si detecta que aun queda algun lugar sin revisar, avisa que aun no se gana
                x=1       ###en caso contrario, avisa que se gano la partida
    if(x==0):
        return True
    else:
        return False

def contar_bombas(lista): ###Funcion para contar cuantas bombas ahi en la proximidad
    x=0
    for i in lista:
        if(i==10): ###Se compara cada valor en cada posicion adjacente, si encuentra algun 10 (valor interno para bombas), lo contabiliza
            x=x+1
    return x

def convertir_letra_numero(letra): ###Entrega el valor numero en el tablero de cada letra
    if(letra=='A'):
        return 0
    elif(letra=='B'):
        return 1
    elif(letra=='C'):
        return 2
    elif(letra=='D'):
        return 3
    elif(letra=='E'):
        return 4
    elif(letra=='F'):
        return 5

def validar_bombas(datos): ###Realiza una validacion de los datos al ingresar las bombas, corroborando que son coordenadas validas
    letras=['A', 'B', 'C', 'D', 'E', 'F']
    numeros=['1', '2', '3', '4', '5', '6']
    if((len(datos)%2!=0) or (len(datos)>6) or (len(datos)<2)): ###Corrobora que sea una cantidad par entre 6 y 2
        return True
    elif(len(datos)==6): ###En caso de ser 6 datos
        if((datos[0] in letras) and (datos[2] in letras) and (datos[4] in letras)): ###Corrobora que alla letras donde debe
            if((datos[1] in numeros) and (datos[3] in numeros) and (datos[5] in numeros)): ###Y con los numeros tambien.  Este proceso se repite para 4 y 2 caracteres
                return False
            else:
                return True
        else:
            return True
    elif(len(datos)==4):
        if((datos[0] in letras) and (datos[2] in letras)):
            if((datos[1] in numeros) and (datos[3] in numeros)):
                return False
            else:
                return True
        else:
            return True
    elif(len(datos)==2):
        if((datos[0] in letras)):
            if((datos[1] in numeros)):
                return False
            else:
                return True
        else:
            return True

def validar_apertura(dato): ###Realiza una validacion de los datos al ingresar un lugar a revisar si ahi bombas
    letras=['A', 'B', 'C', 'D', 'E', 'F']
    numeros=['1', '2', '3', '4', '5', '6']
    if(len(dato)!=2):
        return True
    else:
        if((dato[0] in letras)): ###Si la letra se encuentra entre las opciones validas
            if((dato[1] in numeros)): ###Y el numero tambien se encuentra entre las opciones validas; es entonces que avisa que puede finalizar la validacion
                return False
            else:
                return True
        else:
            return True

def mostrar_tablero_inicial(tablero, letra): ###Muestra el tablero al comenzar la partida
    print("  1 2 3 4 5 6\n")
    for i in range(0, 6):
        print(letra[i] + " ", end="")
        for j in range(0, 6):
            print(".", end="")
            print(" ", end="")
        print("\n")

def mostrar_tablero_actual(tablero, letra): ###Muestra el tablero a lo largo de la partida
    print("  1 2 3 4 5 6\n")
    for i in range(0, 6):
        print(letra[i] + " ", end="")
        for j in range(0, 6):
            if(tablero[i][j]==(-1) or tablero[i][j]==10):
                print(". ", end="")
            else:
                print(tablero[i][j], "", end="")

        print("\n")

def victoria(tablero, letras): ###Muestra el tablero tras finalizada la partida
    print("  1 2 3 4 5 6\n")
    for i in range(0, 6):
        print(letra[i] + " ", end="")
        for j in range(0, 6):
            if(tablero[i][j]==(-1)):
                print(". ", end="")
            elif(tablero[i][j]==10):
                print("* ", end="")
            else:
                print(tablero[i][j], "", end="")

        print("\n")

def colocacion_bombas(tablero, coordenada): ###Funcion para colocar bombas en lugares del tablero
    n=len(coordenada)
    for i in range(0, n, 2):
        if(coordenada[i]=='A'): ###Identifica primero la fila (letra), y luego ingresa la columna (numero)
            tablero[0][int(coordenada[i+1])-1]=10
        elif(coordenada[i]=='B'):
            tablero[1][int(coordenada[i+1])-1]=10
        elif(coordenada[i]=='C'):
            tablero[2][int(coordenada[i+1])-1]=10
        elif(coordenada[i]=='D'):
            tablero[3][int(coordenada[i+1])-1]=10
        elif(coordenada[i]=='E'):
            tablero[4][int(coordenada[i+1])-1]=10
        elif(coordenada[i]=='F'):
            tablero[5][int(coordenada[i+1])-1]=10

def revision(tablero, posicion): ###Funcion para corroborar cantidad de bombas en las proximidades, si se selecciona un lugar con bomba, avisa con un false que perdiste
    x=0
    letra=convertir_letra_numero(posicion[0])
    numero=int(posicion[1])-1
    if(tablero[letra][numero]==10): ###Caso en el que se selecciona una casilla bomba, en la que se pierde automaticamente
        return False
    else:
        if(letra==0):
            if(numero==0): ###Esquina superior izquierda (3 casillas proximas)
                d=[tablero[0][1],tablero[1][1],tablero[1][0]]
                x=contar_bombas(d)
                if(x==0):
                    tablero[letra][numero]=0
                elif(x==1):
                    tablero[letra][numero]=1
                elif(x==2):
                    tablero[letra][numero]=2
                elif(x==3):
                    tablero[letra][numero]=3
            elif(numero==5): ###Esquina superior derecha (3 casillas proximas)
                d=[tablero[0][4],tablero[1][4],tablero[1][5]]
                x=contar_bombas(d)
                if(x==0):
                    tablero[letra][numero]=0
                elif(x==1):
                    tablero[letra][numero]=1
                elif(x==2):
                    tablero[letra][numero]=2
                elif(x==3):
                    tablero[letra][numero]=3
            else: ###Resto de fila A (5 casillas proximas)
                d=[tablero[letra+1][numero-1],tablero[letra+1][numero],tablero[letra+1][numero+1],tablero[letra][numero-1],tablero[letra][numero+1]]
                x=contar_bombas(d)
                if(x==0):
                    tablero[letra][numero]=0
                elif(x==1):
                    tablero[letra][numero]=1
                elif(x==2):
                    tablero[letra][numero]=2
                elif(x==3):
                    tablero[letra][numero]=3
        elif(letra==5):
            if(numero==0): ###Esquina inferior izquierda (3 casillas proximas)
                d=[tablero[5][1],tablero[4][1],tablero[4][0]]
                x=contar_bombas(d)
                if(x==0):
                    tablero[letra][numero]=0
                elif(x==1):
                    tablero[letra][numero]=1
                elif(x==2):
                    tablero[letra][numero]=2
                elif(x==3):
                    tablero[letra][numero]=3
            elif(numero==5): ###Esquina inferior derecha (3 casillas proximas)
                d=[tablero[5][4],tablero[4][4],tablero[4][5]]
                x=contar_bombas(d)
                if(x==0):
                    tablero[letra][numero]=0
                elif(x==1):
                    tablero[letra][numero]=1
                elif(x==2):
                    tablero[letra][numero]=2
                elif(x==3):
                    tablero[letra][numero]=3
            else: ###Resto fila F (5 casillas proximas)
                d=[tablero[letra-1][numero-1],tablero[letra-1][numero],tablero[letra-1][numero+1],tablero[letra][numero-1],tablero[letra][numero+1]]
                x=contar_bombas(d)
                if(x==0):
                    tablero[letra][numero]=0
                elif(x==1):
                    tablero[letra][numero]=1
                elif(x==2):
                    tablero[letra][numero]=2
                elif(x==3):
                    tablero[letra][numero]=3
        elif(numero==0): #Resto columna 1 (5 casillas proximas)
            d=[tablero[letra-1][numero],tablero[letra-1][numero+1],tablero[letra+1][numero],tablero[letra+1][numero+1],tablero[letra][numero+1]]
            x=contar_bombas(d)
            if(x==0):
                tablero[letra][numero]=0
            elif(x==1):
                tablero[letra][numero]=1
            elif(x==2):
                tablero[letra][numero]=2
            elif(x==3):
                    tablero[letra][numero]=3
        elif(numero==5): ###Resto columna 5 (5 casillas proximas)
            d=[tablero[letra+1][numero],tablero[letra+1][numero-1],tablero[letra-1][numero],tablero[letra-1][numero-1],tablero[letra][numero-1]]
            x=contar_bombas(d)
            if(x==0):
                tablero[letra][numero]=0
            elif(x==1):
                tablero[letra][numero]=1
            elif(x==2):
                tablero[letra][numero]=2
            elif(x==3):
                tablero[letra][numero]=3
        else: ###Todos los demas caso (8 casillas proximas)
            d=[tablero[letra][numero-1],tablero[letra][numero+1],tablero[letra+1][numero-1],tablero[letra+1][numero],
               tablero[letra+1][numero+1],tablero[letra-1][numero-1],tablero[letra-1][numero],tablero[letra-1][numero+1]]
            x=contar_bombas(d)
            if(x==0):
                tablero[letra][numero]=0
            elif(x==1):
                tablero[letra][numero]=1
            elif(x==2):
                tablero[letra][numero]=2
            elif(x==3):
                tablero[letra][numero]=3
        return True
    
###################################################################  Main  ################################################################
terminar=True
valido=True
tablero=[
    [-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1]
]
letra=['A','B','C','D','E','F']
mostrar_tablero_inicial(tablero, letra)

while(valido): ###Ciclo para validar posicion de las bombas
    colocacion=str(input("Ingrese las coordenadas de las bombas (Max. 3 coordenadas): "))
    colocacion=colocacion.upper()
    valido=validar_bombas(colocacion)
    
valido=True
colocacion_bombas(tablero, colocacion) ###Se colocan las bombas

while(terminar): ###Ciclo para el funcionamiento del juego
    valido=True
    
    while(valido): ###Ciclo para validar corroboracion de casilla a reviar
        apertura=str(input("Ingrese bloque a revisar:"))
        apertura=apertura.upper()
        valido=validar_apertura(apertura)
    terminar=revision(tablero, apertura)
    
    if(terminar==False): ###En caso de tocar una bomba
        victoria(tablero, letra)
        print("PERDISTE.")
        break
    
    if(verificar_victoria(tablero)): ###En caso de ganar el juego
        victoria(tablero, letra)
        print("GANASTE!")
        break
    
    else: ###En caso de no perder ni ganar aun
        mostrar_tablero_actual(tablero, letra)
    
