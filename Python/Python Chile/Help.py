def mcd(n1, n2): # escribe tu función aquí, recuerda seguir cuidadosamente
# las instrucciones respecto a argumentos y retorno
    mcd = 1
    resultado = 0
    menor = 0
    if n1 < n2:
        menor = n1
    else :
        menor = n2
    for i in range(1,menor+1):
        if n1%i == 0 and n2%i == 0:
            mcd = i
    return mcd

def exponente(n):# escribe tu función aquí, recuerda seguir cuidadosamente
# las instrucciones respecto a argumentos y retorno
    ayuda = 0
    for i in range(n+1):
        if 2**i <= n:
            ayuda = i
    return ayuda
        
def opcion_menu(N):
  opcion = int(input("Ingresa opción desde 0 a "+str(N-1)+": "))
  while opcion < 0 or opcion > N-1:
    #print("Inténtalo otra vez.")
    opcion = int(input("Ingresa opción desde 0 a "+str(N-1)+": "))
  return opcion

def panprimo(n):# escribe tu función aquí, recuerda seguir cuidadosamente
# las instrucciones respecto a argumentos y retorno
    tn = str(n)
    result = False
    for i in range(10):
        if str(i) in tn:
            result = True
        else: 
            result = False
    if result == False:
        return False
    else:
        cadena = ""
        new_n = n//1000
        tnew = str(new_n)
        for i in range(0, 10):
            if str(i) in tn and not(str(i) in tnew):
                cadena += str(i)
        primo = int(cadena)
        #print(primo)
        return True

s = "Acaso hubo buhos aca"
t = s[2:9]+s[0:1]
#print(t)

def mezclador(string_a, string_b):
  # aquí debes escribir el código de tu programa
  return string_a[0:2] + string_b[len(string_b)-2:len(string_b)]

#print(mezclador("familia", "abrogarRE"))

def intercalar(string_a, string_b): 
  result = ""
  for i in range(len(string_a)):
    result += string_a[i] + string_b
  return result # aquí debes retornar el resultado

#print(intercalar("paz", "sol"))

def ocurrencias(string):
  ones = 0
  zero = 0
  for i in range(len(string)):
    if string[i] == "1":
      ones = ones + 1
    elif string[i]== "0":
      zero = zero + 1
  return ones-zero # aquí debes retornar el resultado

#print(ocurrencias("11000110101"))

def remover_enesimo(s, n):
  result = ""
  for i in range(len(s)):
    if i != n:
      result += s[i]
  return result

#print(remover_enesimo("Hasta luego", 0))

def reemplazo(string):
  result = ""
  abc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
  can = False
  for j in range(len(string)):
    a = string[j]
    if a in abc:
      result += "$"
    else: 
      result += a
  return result #

#print(reemplazo("Com te V"A))

import math as m

def promedio_std(lista): # debes modificar todos los elementos de la función
	# cuidando el retorno, nombre y argumentos
	suma = 0
	diferencia = 0
	allDifference = 0
	for x in lista:
		suma += int(x)
	promedio = suma/len(lista)
	for element in lista:
		if element > promedio:
			diferencia = promedio - element
		else:
			diferencia = promedio - element
		allDifference += diferencia*diferencia
	print(allDifference)
	endDifference = (allDifference/len(lista))**(0.5)
	return (promedio, endDifference)

a = [99, 53, 6, 92, 98, 26, 17, 10, 82, 32]
print(promedio_std(a))

def color_frecuente(lista):
	counterBlue = 0
	counterRed = 0
	counterGreen = 0
	counterYellow = 0
	for element in lista:
		if element == "rojo":
			counterRed += 1
		elif element == "azul":
			counterBlue += 1
		elif element == "verde":
			counterGreen += 1
		elif element == "amarillo":
			counterYellow += 1
	counters = [[counterRed, "rojo"], [counterYellow, "amarillo"], [counterGreen, "verde"], [counterBlue, "azul"]]
	counters.sort()
	last = counters[len(counters)-1]
	antepenultimate = counters[len(counters)-2]
	if last[0] == antepenultimate[0]:
		if antepenultimate[1] < last[1]:
			return antepenultimate[1], antepenultimate[0]
		else:
			return last[1], last[0]
	else:
		return last[1], last[0]

#a = ['azul', 'rojo', 'verde', 'verde', 'verde', 'rojo', 'verde', 'verde', 'azul', 'amarillo', 'azul', 'azul', 'verde', 'verde', 'verde', 'amarillo', 'amarillo']
a = ['rojo', 'rojo', 'verde', 'rojo', 'rojo', 'rojo', 'azul', 'rojo', 'azul', 'rojo', 'azul', 'azul', 'rojo', 'azul', 'rojo', 'azul', 'azul', 'azul', 'azul', 'rojo', 'rojo', 'azul', 'verde', 'verde', 'azul', 'azul', 'rojo', 'rojo', 'rojo', 'azul', 'amarillo', 'azul', 'azul', 'rojo']
#print(type(a))
print(color_frecuente(a))

def buscaminas(tablero, i, j):
	minas = 0
	if i == 0:
		if j == len(tablero[1])-1:
			if tablero[i][j-1] == "X":
				minas += 1
			if tablero[i+1][j-1] == "X":
				minas += 1
			if tablero[i+1][j] == "X":
				minas += 1
		if j == 0:
			if tablero[i+1][j] == "X":
				minas += 1
			if tablero[i+1][j+1] == "X":
				minas += 1
			if tablero[i][j+1] == "X":
				minas += 1
		else:
			if tablero[i][j-1] == "X":
				minas += 1
			if tablero[i+1][j-1] == "X":
				minas += 1
			if tablero[i+1][j] == "X":
				minas += 1
			if tablero[i+1][j+1] == "X":
				minas += 1
			if tablero[i][j+1] == "X":
				minas += 1
	elif i == len(tablero[1])-1:
		if j == len(tablero[1])-1:
			if tablero[i][j-1] == "X":
				minas += 1
			if tablero[i-1][j-1] == "X":
				minas += 1
			if tablero[i-1][j] == "X":
				minas += 1
		if j == 0:
			if tablero[i-1][j] == "X":
				minas += 1
			if tablero[i][j+1] == "X":
				minas += 1
			if tablero[i-1][j+1] == "X":
				minas += 1
		else:
			if tablero[i][j-1] == "X":
				minas += 1
			if tablero[i-1][j-1] == "X":
				minas += 1
			if tablero[i-1][j] == "X":
				minas += 1
			if tablero[i-1][j+1] == "X":
				minas += 1
			if tablero[i][j+1] == "X":
				minas += 1
	else:
		if tablero[i-1][j-1] == "X":
				minas += 1
		if tablero[i][j-1] == "X":
				minas += 1
		if tablero[i+1][j-1] == "X":
				minas += 1
		if tablero[i+1][j] == "X":
				minas += 1
		if tablero[i+1][j+1] == "X":
				minas += 1
		if tablero[i][j+1] == "X":
				minas += 1
		if tablero[i-1][j+1] == "X":
				minas += 1
		if tablero[i-1][j] == "X":
				minas += 1
	return minas

a =[[' ', 'X', ' ', 'X'],['X', ' ', ' ', ' '],[' ', 'X', 'X', ' '],['X', ' ', ' ', 'X']]
#print(a)
print(buscaminas(a, 0,1))