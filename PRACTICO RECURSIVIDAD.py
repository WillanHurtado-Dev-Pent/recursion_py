# PRACTICO RECURSIVIDAD
# A) NÚMEROS
# 1)ESCRIBIR UNA FUNCION QUE DEVUELVA EL MAYOR DE LOS DIGITOS DE UN NUMERO:
def OBT_digito_mayor(nro):
    if (nro > 0 and nro < 10):
        return nro
    dig_a = nro % 10
    nro = nro // 10
    dig_b = nro % 10
    if (dig_a > dig_b):
        nro = nro - dig_b
        nro = nro + dig_a
    return OBT_digito_mayor(nro)
n = int(input("Ingrese un numero:"))
print(OBT_digito_mayor(n))


# 2)ESCRIBIR UNA FUNCION QUE DEVUELVA LA SUMA DE LOS DIGITOS PARES DE UN NUMERO
def sum_pares(num):
    sum = 0
    if 0 < num < 10:
        if num % 2 == 0:
            sum = num
        else:
            sum = 0
    else:
        dig = num % 10
        num = num // 10
        sum = sum_pares(num)
        if ((dig % 2) == 0):
            sum = sum + (dig)
    return sum
num=int(input("Digite un número: "))
print("La suma de los digitos pares es: " , sum_pares(num))

# 3)Escribir un proceso que lleve el mayor de los dígitos al final de un número.
#Ej. x=382731; MoverMayor(x); x=32
def sacar_primer_digito(n):
    if n< 10 :
        return n
    else:
        return sacar_primer_digito(int(n/10))

def sacar_primer_iesimo(n):
    if n< 10 :
        return n
    else:
        return sacar_primer_iesimo(int(n/10))*10
def digito_mayor(n):
    if (n<10):
        return n
    else:
        ud= n % 10
        if (ud > digito_mayor(int(n/10)) ):
            return ud
        else:
            return digito_mayor(int(n/10))
def MoverMayor(x):
    if (x<10):
        return x
    else:
        pri_dig=sacar_primer_digito(x)
        pri_ies=sacar_primer_iesimo(x)
        resto=x-pri_ies
        if (pri_dig > digito_mayor(resto) ):
            return (resto *10) +pri_dig
        elif (pri_dig ==digito_mayor(resto ) ):
            return (MoverMayor(resto )*10 ) + pri_dig
        else:
            return pri_ies + MoverMayor(resto )
n=int(input("Dame un número: ") )
print(MoverMayor(n))


# 4)ESCRIBIR UN NUMERO QUE DEVUELVA TRUE SI UN NUMERO ESTA ORDENADO EN SUS DIGITOS
def esta_ord(num):
    if num < 10:
        sw = True
    else:
        d = num % 10
        num = num / 10
        sw = esta_ord(num)
        if sw:
            if d >= num % 10:
                sw = True
            else:
                sw = False
    return sw
num=int(input("Digite un número: "))
print(esta_ord(num))

# 5)ESCRIBIR UNA FUNCION QUE DEVUELVA LA CANTIDAD DE DIGITOS IMPARES QUE ESTAN ANTES DE UNO PAR
def CantDigImparesAntesPar(nro):
    if nro >= 10:
        dig_a = nro % 10
        nro = nro // 10
        dig_b = nro % 10
        if dig_a % 2 != 0 and dig_b % 2 == 0:
            return CantDigImparesAntesPar(nro) + 1
        else:
            return CantDigImparesAntesPar(nro)
    else:
        return 0
n = int(input("Ingrese el numero:"))
print(CantDigImparesAntesPar(n))

# B) SERIES
# 1)ESCRIBIR UNA FUNCION QUE DEVUELVA EL N-SIMO TERMINO DE LA SERIE DE FIBONACCI   0,1,1,2,3,5,8,13
def fibonacci_recursivo(pos):
    if(pos == 1):
        return 0
    elif(pos == 2):
        return 1
    return fibonacci_recursivo(pos-1) + fibonacci_recursivo(pos-2)

n = int(input("digite un numero=> "))
print(fibonacci_recursivo(n))

# 2)ESCRIBIR UNA FUNCION QUE DEVUELVA EL N-SIMO TERMINO DE LA SIGUIENTE SERIE
# 1,2,3,6,7,14,15,30,31
def ser2(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    elif n % 2 == 0:
        return ser2(n - 1) * 2
    else:
        return ser2(n - 1) + 1


n = int(input("Ingrese un numero: "))
print(ser2(n))

# 3) Escribir una función que devuelva la suma de los primeros n términos de la siguiente serie: 0, 2, 4, 6, 8, 10
def sum_par_rec(pos):
    if pos == 0:
        return 0
    else:
        return sum_par_rec(pos-1) + 2*(pos-1)

n = int(input("Ingrese un numero: "))
print(sum_par_rec(n))

# 4)ESCRIBIR UNA FUNCION QUE DEVUELVA EL N-SIMO TERMINO DE LA SIGUIENTE SERIE
# s = 1,3,7,15,31,63,127,255
sem = 1
n=int(input("deme el numero de la serie que quiere generar: "))
def sum_serie_par(n):
    if n == 1:
        return sem
    else:
        return (sum_serie_par(n-1)*2)+1
print(sum_serie_par(n))

# 5)Escribir una función que devuelva la suma de los terminos pares de la siguiente serie: 1,2,4,5,10,12,13,26,28,29
def Serie2(pos):
    if pos == 0:
        return 0
    else:
        if pos % 3 == 0:
            return Serie2(pos - 1) + 2
        elif (pos + 1) % 3 == 0:
            return Serie2(pos - 1) * 2
        else:
            return Serie2(pos - 1) + 1

def sum_serie2(x):
    if x == 0:
        return 0
    else:
        if(Serie2(x)%2==0):
            return sum_serie2(x-1) + Serie2(x)
        else:
            return sum_serie2(x-1)

n = int(input("ingrese digitos de la serie a guardar: "))
print(sum_serie2(n))


# C) CADENAS
# 1) ESCRIBIR UNA FUNCION QUE DEVUELVA LA CANTIDAD DE PALABRAS QUE HAY EN UNA CADENA CANTPAL("HOLA BUENAS TARDES")=3
def Cont_Pal(cad):
    if cad == "":
        return 0
    if len(cad) == 1:
        return 1
    if cad[0] == " ":
        return 1 + Cont_Pal(cad[1:])
    else:
        return Cont_Pal(cad[1:])

cad = input("Ingrese una cadena:")
print(Cont_Pal(cad))

# 2) ESCRIBIR UN PROCESO QUE ELIMINE LAS VOCALES DE UNA CADENA Ej. x=”Buenas tardes”; EliminarVoc(x); x=”Bns trds”
def EliminarVocales(cad):
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    if cad == "":
        return cad
    if cad[0] in vocales:
        return ""  + EliminarVocales(cad[1:])
    else:
        return cad[0] + EliminarVocales(cad[1:])
cad = input("Ingrese la cadena:")
print(EliminarVocales(cad))

# 3) Escribir una función que devuelva la palabra más larga de una cadena
# Ej. CadenaMasLarga(“esta es una prueba más”)  “prueba”
def palabra_mas_larga_rec(cad):
    pos = 0
    cant_car_izq = 0
    cant_car_der = 0
    cond_2da_palabra = True
    ultima_pos_cad = sum([1 for _ in cad]) - 1

    if ' ' not in cad:
        return cad
    else:
        while cad[pos] != ' ':
            cant_car_izq += 1
            pos += 1

        pos += 1
        while cond_2da_palabra:
            if pos <= ultima_pos_cad:
                if cad[pos] != ' ':
                    cant_car_der += 1
                    pos += 1
                else:
                    cond_2da_palabra = False
            else:
                cond_2da_palabra = False

        if cant_car_izq > cant_car_der:
            cad = cad[: cant_car_izq] + cad[pos:]
        else:
            cad = cad[pos - cant_car_der:]

        return palabra_mas_larga_rec(cad)

cadena = "ESTA ES UNA PRUEBA MAS"
print(palabra_mas_larga_rec(cadena))

# 4)Escribir un proceso para eliminar la primera letra de cada palabra
cadena=input("digite una cadena: ")
cadena=" "+cadena
tam=len(cadena)

def esSeparador(car):
    return (car==" " or car=="," or car==";" or car=="." or car=="\n" or car=="\t")
def eliminarPrim(cad):
    tama=len(cad)
    if (tama==2):
        return ""
    else:
        if (esSeparador(cad[tama-2]) and not  (esSeparador(cad[tama-1]))):
            return eliminarPrim(cad[:tama-1])
        else:
            return (eliminarPrim(cad[:tama-1]))+cad[tama-1]
cad=eliminarPrim(cadena)
print(cad)

# 5) Invertir una cadena
def inv_cad(cadena):
    if len(cadena)==1:
        return cadena
    else:
        return cadena[-1]+inv_cad(cadena[:-1])
cad=input("digite una oracion: ")
print(inv_cad(cad))

# D) VECTORES
# 1)ESCRIBIR UNA FUNCION QUE DEVUELVA LA CANTIDAD DE NUMEROS PARES QUE CONTIENE
def contar_parv(vec):
    if vec == []:
        return 0
    else:
        if vec[0]%2 == 0:
            vec = vec[1:]
            return contar_parv(vec) + 1
        else:
            vec = vec[1:]
            return contar_parv(vec)

vec = [2,4,5,12,23,54,3,34,6]
print(contar_parv(vec))

# 2) ESCRIBIR UN PROCESO PARA ORDENAR UN VECTOR. CON EL ALGORITMO MERGESORT
def merge_sort(lista):
    """
    Lo primero que se ve en el psudocódigo es un if que
    comprueba la longitud de la lista. Si es menor que 2, 1 o 0, se devuelve la lista.
    ¿Por que? Ya esta ordenada.
    """
    if len(lista) < 2:
        return lista
    # De lo contrario, se divide en 2
    else:
        mitad = len(lista) // 2
        derecha = merge_sort(lista[:mitad])
        izquierda = merge_sort(lista[mitad:])
        return merge(derecha, izquierda)
# Función merge
def merge(lista1, lista2):
    """
    merge se encargara de intercalar los elementos de las dos
    divisiones.
    """
    i, j = 0, 0  # Variables de incremento
    result = []  # Lista de resultado
    # Intercalar ordenadamente
    while (i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            result.append(lista1[i])
            i += 1
        else:
            result.append(lista2[j])
            j += 1
    # Agregamos los resultados a la lista
    result += lista1[i:]
    result += lista2[j:]
    # Retornamos el resultados
    return result
# Prueba del algoritmo
lista = [31, 3, 88, 1, 4, 2, 42]
merge_sort_result = merge_sort(lista)
print(merge_sort_result)

# 3) ESCRIBIR UN PROCESO PARA ORDENAR UN VECTOR. CON EL ALGORITMO INSERTIONSORT

def insertionSortRecursive(vec,n):
    if n <= 1:
        return
    insertionSortRecursive(vec,n-1)
    ult = vec[n - 1]
    j = n - 2
    while (j >= 0 and vec[j] > ult):
        vec[j + 1] = vec[j]
        j = j - 1
    vec[j + 1] = ult
vect=[]
def printArray(vec,n):
    for i in range(n):
        vect.append(vec[i])
    print(vect)
vec= [12,11,13,5,6]
n = len(vec)
insertionSortRecursive(vec, n)
printArray(vec,n)

# 4) ESCRIBIR UN PROCESO PARA ELIMINAR EL DATO X DE UN VECTOR EJ:V[2,5,65,23,45,2,13,45,61] X = 2 ---> V[5,65,23,45,13,45,61]
def elim_x(vec):
    if x in vec:
        if vec[0] == x:
            vec = vec[1:]
            return elim_x(vec)
        else:
            vec2.append(vec[0])
            vec = vec[1:]
            return elim_x(vec)
    else:
        if vec == []:
            return vec2
        else:
            vec2.append(vec[0])
            vec = vec[1:]
            return elim_x(vec)
vec = []
n = int(input("Ingrese la cantidad de elementos de su vector:"))
def cargar_vector(pos):
    if pos < n:
        dato=int(input(f"deme el elemnto {pos}:"))
        vec.append(dato)
        cargar_vector(pos+1)
cargar_vector(0)
x = int(input("Ingrese el x a eliminar:"))
vec2 = []
print(elim_x(vec))

# 5) ESCRIBIR UN PROCESO PARA INVERTIR UNA PARTE DE UN VECTOR ( ENTRE A Y B)
v = [2,5,65,23,45,2,13,45]
a = int(input("Deme el limite inferior a invertir: "))
b = int(input("Deme el limite superior a invertir: "))

def invertir_rango(a,b):
    if a<b:
        aux = v[a]
        aux2 = v[b]
        v[a] = aux2
        v[b] = aux
        invertir_rango(a+1,b-1)

tam = len(v)
if (a<b)and(b<tam):
    invertir_rango(a,b)
print(v)


# E) MATRICES
# ESCRIBIR PROCESO PARA CARGAR MATRICES DE LA SIGUIENTE FORMA:
# 1) DEL PRACTICO
tam = int(input("Ingrese la dimension de la matriz: "))
matriz = []
aux = [0]
aux2 = [1]
def crear(t):
    vacia = list(range(tam))
    matriz.append(vacia)
    if (t > 1):
        crear(t - 1)
def vaciar(t):
    matriz[t-1][aux2[0]-1] = 0
    aux2[0] = aux2[0] + 1
    if (t != 1) or (aux2[0] != (tam+1)):
        if aux2[0] == tam + 1:
            aux2[0] = 1
            vaciar(t-1)
        else:
            vaciar(t)
def llenar_columna(lugar,t):
    matriz[t-1][lugar-1] = aux[0] + 1
    aux[0] = aux[0] + 1
    if lugar > 1:
        llenar_columna(lugar-1,t)
def llenar_fila(t):
    tamaño = t
    llenar_columna(tamaño,t)
    if (t>1):
        llenar_fila(t-1)
crear(tam)
vaciar(tam)
llenar_fila(tam)
for i in range(tam):
    print(matriz[i],"\n")

# 2) DEL PRACTICO
tam = int(input("Ingrese la dimension de la matriz: "))
matriz = []
aux = [0]
aux2 = [1]
def crear(t):
    vacia = list(range(tam))
    matriz.append(vacia)
    if (t > 1):
        crear(t - 1)

def vaciar(t):
    matriz[t-1][aux2[0]-1] = 0
    aux2[0] = aux2[0] + 1
    if (t != 1) or (aux2[0] != (tam+1)):
        if aux2[0] == tam + 1:
            aux2[0] = 1
            vaciar(t-1)
        else:
            vaciar(t)

def cargar_mat(m, fil, col, val):
    if col == m-1:
        return 0
    else:
        if fil == m:
            col += 1
            fil = col
        matriz[fil][col] = val
        if fil < m:
            fil += 1
        return cargar_mat(m, fil, col, val+1)

def imprimir_matriz(m):
    if m == 1:
        print(matriz[tam - m])
    else:
        print(matriz[tam - m])
        imprimir_matriz(m - 1)

crear(tam)
vaciar(tam)
fil = 0
col = 0
val = 1
cargar_mat(tam, fil, col, val)
imprimir_matriz(tam)

# 3) DEL PRACTICO
tam = int(input("Ingrese la dimension de la matriz: "))
tam2 = int(input("Ingrese la dimension de la matriz: "))
matriz = []
def crear(t):
    vacia = list(range(tam2))
    matriz.append(vacia)
    if (t > 1):
        crear(t - 1)

def cargar_en_espiral(m, n, fil, col, val):
    if col < 0:
        return 0
    else:
        matriz[fil][col] = val
        fil = fil + ((-1) ** (col + 1))

        if (fil == -1):
            fil = 0
            col -= 1
        if fil == m:
            fil = m - 1
            col -= 1
        return cargar_en_espiral(m, n, fil, col, val - 1)

def ini_cargar_en_espiral():
    if tam % 2 == 0:
        fil = tam - 1
    else:
        fil = 0
    col = tam2 - 1
    val = tam * tam2
    cargar_en_espiral(tam, tam2, fil, col, val)

def imprimir_matriz(m):
    if m == 1:
        print(matriz[tam - m])
    else:
        print(matriz[tam - m])
        imprimir_matriz(m - 1)

crear(tam)
ini_cargar_en_espiral()
imprimir_matriz(tam)
# 4) DEL PRACTICO
tam = int(input("Ingrese la dimension de la matriz: "))
matriz = []
aux = [0]
aux2 = [1]
contador = 1
i = 0
j = tam // 2
contador = 1
long = tam*tam

def crear(t):
    vacia = list(range(tam))
    matriz.append(vacia)
    if (t > 1):
        crear(t - 1)

def vaciar(t):
    matriz[t-1][aux2[0]-1] = 0
    aux2[0] = aux2[0] + 1
    if (t != 1) or (aux2[0] != (tam+1)):
        if aux2[0] == tam + 1:
            aux2[0] = 1
            vaciar(t-1)
        else:
            vaciar(t)

def magico_impar(long,n,i,j,contador,arreglo):
    if contador < long:
        if ((i - 1) >= 0):
            if ((j + 1) < (n)):
                if (arreglo[i - 1][j + 1] == 0):
                    i -= 1
                    j += 1
                    contador += 1
                    arreglo[i][j] = contador
                    return magico_impar(long,n,i,j,contador,arreglo)
                else:
                    i += 1
                    contador += 1
                    arreglo[i][j] = contador
                    return magico_impar(long, n, i, j, contador, arreglo)
            else:
                if (arreglo[i - 1][0] == 0):
                    i -= 1
                    j = 0
                    contador += 1
                    arreglo[i][j] = contador
                    return magico_impar(long, n, i, j, contador, arreglo)
                else:
                    i += 1
                    contador += 1
                    arreglo[i][j] = contador
                    return magico_impar(long, n, i, j, contador, arreglo)
        else:
            if (((j + 1) < (n))):
                if (arreglo[n - 1][j + 1] == 0):
                    i = n - 1
                    j += 1
                    contador += 1
                    arreglo[i][j] = contador
                    return magico_impar(long, n, i, j, contador, arreglo)
                else:
                    i += 1
                    contador += 1
                    arreglo[i][j] = contador
                    return magico_impar(long, n, i, j, contador, arreglo)
            else:
                i += 1
                contador += 1
                arreglo[i][j] = contador
                return magico_impar(long, n, i, j, contador, arreglo)
    else:
        return 0

def imprimir_matriz(m):
    if m == 1:
        print(matriz[tam - m])
    else:
        print(matriz[tam - m])
        imprimir_matriz(m - 1)

crear(tam)
vaciar(tam)
matriz[i][j] = 1
magico_impar(long,tam,i,j,contador,matriz)
imprimir_matriz(tam)


# 5) DEL PRACTICO
m = int(input("Ingrese la dimension de la matriz: "))
tam = m
matriz = []

def formar_vacia(m):
    vacia = list(range(tam))
    if m == 1:
        matriz.append(vacia)
    else:
        matriz.append(vacia)
        formar_vacia(m - 1)

def llenar_fila(n,m):
    if n == 1:
        matriz[0][m-1] = tam - m + 1
    else:
        matriz[n-1][m-1] = tam - m + 1
        llenar_fila(n-1,m)

def llenar_columna(m,n):
    if n == 1:
        matriz[m-1][0] = tam - m + 1
    else:
        matriz[m-1][n-1] = tam - m + 1
        llenar_columna(m,n-1)

def formar_matriz(m):
    if m == 1:
        matriz[0][0] = tam - m + 1
    else:
        llenar_fila(m, m)
        llenar_columna(m, m)
        formar_matriz(m - 1)

def imprimir_matriz(m):
    if m == 1:
        print(matriz[tam - m])
    else:
        print(matriz[tam - m])
        imprimir_matriz(m - 1)

def cuadrado_matriz(m):
    formar_vacia(m)
    formar_matriz(m)
    imprimir_matriz(m)

cuadrado_matriz(m)


