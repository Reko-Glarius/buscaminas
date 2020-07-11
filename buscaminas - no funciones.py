###################################################################  Main  ################################################################
###Variables
sw=0
letras=['A', 'B', 'C', 'D', 'E', 'F']
numeros=['1', '2', '3', '4', '5', '6']
terminar=True
valido=True
victoria=False
tablero=[
    [-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1]
]

###Primera muestra del tablero
print("  1 2 3 4 5 6\n")
for i in range(0, 6):
    print(letras[i] + " ", end="")
    for j in range(0, 6):
        print(".", end="")
        print(" ", end="")
    print("\n")
    
###Ciclo de ingreso de bombas, esta es validada
while(valido): 
    datos=str(input("Ingrese las coordenadas de las bombas (Max. 3 coordenadas): "))
    datos=datos.upper()
    ###Comienza validacion
    if((len(datos)%2!=0) or (len(datos)>6) or (len(datos)<2)): 
        valido=True
    elif(len(datos)==6): 
        if((datos[0] in letras) and (datos[2] in letras) and (datos[4] in letras)): 
            if((datos[1] in numeros) and (datos[3] in numeros) and (datos[5] in numeros)): 
                valido=False
            else:
                valido=True
        else:
            valido=True
    elif(len(datos)==4):
        if((datos[0] in letras) and (datos[2] in letras)):
            if((datos[1] in numeros) and (datos[3] in numeros)):
                valido=False
            else:
                valido=True
        else:
            valido=True
    elif(len(datos)==2):
        if((datos[0] in letras)):
            if((datos[1] in numeros)):
                valido=False
            else:
                valido=True
        else:
            valido=True
            
###Se re establecen valores y se convierte letras en numeros   
valido=True
n=len(datos)
for i in range(0, n, 2):
    if(datos[i]=='A'): 
        tablero[0][int(datos[i+1])-1]=10
    elif(datos[i]=='B'):
        tablero[1][int(datos[i+1])-1]=10
    elif(datos[i]=='C'):
        tablero[2][int(datos[i+1])-1]=10
    elif(datos[i]=='D'):
        tablero[3][int(datos[i+1])-1]=10
    elif(datos[i]=='E'):
        tablero[4][int(datos[i+1])-1]=10
    elif(datos[i]=='F'):
        tablero[5][int(datos[i+1])-1]=10

###Ciclo del juego
while(terminar): 
    valido=True
    ###Muestra de tablero actual e ingreso de coordenada a a revisar (con validacion de esta)
    while(valido):
        ###Muestra tablerop actualmente
        print("  1 2 3 4 5 6\n")
        for i in range(0, 6):
            print(letras[i] + " ", end="")
            for j in range(0, 6):
                if(tablero[i][j]==(-1) or tablero[i][j]==10):
                    print(". ", end="")
                else:
                    print(tablero[i][j], "", end="")
            print("\n")

        ##Soliciud de coordenada
        apertura=str(input("Ingrese bloque a revisar:"))
        apertura=apertura.upper()
        ###Validacion coordenada
        if(len(apertura)!=2):
            valido=True
        else:
            if((apertura[0] in letras)): 
                if((apertura[1] in numeros)): 
                    valido=False
                else:
                    valido=True
            else:
                valido=True
                
    ###Inicializacion de variable para contar bombas en la cercania
    x=0
    ###conversion letra a numero
    if(apertura[0]=='A'):
        letra=0
    elif(apertura[0]=='B'):
        letra=1
    elif(apertura[0]=='C'):
        letra=2
    elif(apertura[0]=='D'):
        letra=3
    elif(apertura[0]=='E'):
        letra=4
    elif(apertura[0]=='F'):
        letra=5
    numero=int(apertura[1])-1

    ###Inicio revision casillas cercanas y caso de pisa una mina
    if(tablero[letra][numero]==10): 
        terminar=False
    else:
        if(letra==0):
            if(numero==0): 
                d=[tablero[0][1],tablero[1][1],tablero[1][0]]
                x=0
                for i in d:
                    if(i==10): 
                        x=x+1
                if(x==0):
                    tablero[letra][numero]=0
                elif(x==1):
                    tablero[letra][numero]=1
                elif(x==2):
                    tablero[letra][numero]=2
                elif(x==3):
                    tablero[letra][numero]=3
            elif(numero==5): 
                d=[tablero[0][4],tablero[1][4],tablero[1][5]]
                x=0
                for i in d:
                    if(i==10): 
                        x=x+1
                if(x==0):
                    tablero[letra][numero]=0
                elif(x==1):
                    tablero[letra][numero]=1
                elif(x==2):
                    tablero[letra][numero]=2
                elif(x==3):
                    tablero[letra][numero]=3
            else: 
                d=[tablero[letra+1][numero-1],tablero[letra+1][numero],tablero[letra+1][numero+1],tablero[letra][numero-1],tablero[letra][numero+1]]
                x=0
                for i in d:
                    if(i==10): 
                        x=x+1
                if(x==0):
                    tablero[letra][numero]=0
                elif(x==1):
                    tablero[letra][numero]=1
                elif(x==2):
                    tablero[letra][numero]=2
                elif(x==3):
                    tablero[letra][numero]=3
        elif(letra==5):
            if(numero==0): 
                d=[tablero[5][1],tablero[4][1],tablero[4][0]]
                x=0
                for i in d:
                    if(i==10): 
                        x=x+1
                if(x==0):
                    tablero[letra][numero]=0
                elif(x==1):
                    tablero[letra][numero]=1
                elif(x==2):
                    tablero[letra][numero]=2
                elif(x==3):
                    tablero[letra][numero]=3
            elif(numero==5): 
                d=[tablero[5][4],tablero[4][4],tablero[4][5]]
                x=0
                for i in d:
                    if(i==10): 
                        x=x+1
                if(x==0):
                    tablero[letra][numero]=0
                elif(x==1):
                    tablero[letra][numero]=1
                elif(x==2):
                    tablero[letra][numero]=2
                elif(x==3):
                    tablero[letra][numero]=3
            else: 
                d=[tablero[letra-1][numero-1],tablero[letra-1][numero],tablero[letra-1][numero+1],tablero[letra][numero-1],tablero[letra][numero+1]]
                x=0
                for i in d:
                    if(i==10): 
                        x=x+1
                if(x==0):
                    tablero[letra][numero]=0
                elif(x==1):
                    tablero[letra][numero]=1
                elif(x==2):
                    tablero[letra][numero]=2
                elif(x==3):
                    tablero[letra][numero]=3
        elif(numero==0): 
            d=[tablero[letra-1][numero],tablero[letra-1][numero+1],tablero[letra+1][numero],tablero[letra+1][numero+1],tablero[letra][numero+1]]
            x=0
            for i in d:
                if(i==10): 
                    x=x+1
            if(x==0):
                tablero[letra][numero]=0
            elif(x==1):
                tablero[letra][numero]=1
            elif(x==2):
                tablero[letra][numero]=2
            elif(x==3):
                    tablero[letra][numero]=3
        elif(numero==5): 
            d=[tablero[letra+1][numero],tablero[letra+1][numero-1],tablero[letra-1][numero],tablero[letra-1][numero-1],tablero[letra][numero-1]]
            x=0
            for i in d:
                if(i==10): 
                    x=x+1
            if(x==0):
                tablero[letra][numero]=0
            elif(x==1):
                tablero[letra][numero]=1
            elif(x==2):
                tablero[letra][numero]=2
            elif(x==3):
                tablero[letra][numero]=3
        else: 
            d=[tablero[letra][numero-1],tablero[letra][numero+1],tablero[letra+1][numero-1],tablero[letra+1][numero],
               tablero[letra+1][numero+1],tablero[letra-1][numero-1],tablero[letra-1][numero],tablero[letra-1][numero+1]]
            x=0
            for i in d:
                if(i==10): 
                    x=x+1
            if(x==0):
                tablero[letra][numero]=0
            elif(x==1):
                tablero[letra][numero]=1
            elif(x==2):
                tablero[letra][numero]=2
            elif(x==3):
                tablero[letra][numero]=3
        terminar=True
        
    x=0
    ###Corroboracion de victoria
    for fila in tablero:
        for dato in fila:
            if(dato==-1): 
                x=1       
    if(x==0):
        victoria=True

    ###En caso de perder
    if(terminar==False): 
        print("  1 2 3 4 5 6\n")
        for i in range(0, 6):
            print(letras[i] + " ", end="")
            for j in range(0, 6):
                if(tablero[i][j]==(-1)):
                    print(". ", end="")
                elif(tablero[i][j]==10):
                    print("* ", end="")
                else:
                    print(tablero[i][j], "", end="")
            print("\n")
        print("PERDISTE.")
        break

    ###En caso de ganar
    if(victoria==True): 
        print("  1 2 3 4 5 6\n")
        for i in range(0, 6):
            print(letras[i] + " ", end="")
            for j in range(0, 6):
                if(tablero[i][j]==(-1)):
                    print(". ", end="")
                elif(tablero[i][j]==10):
                    print("* ", end="")
                else:
                    print(tablero[i][j], "", end="")
            print("\n")
        print("GANASTE!")
        break
    
