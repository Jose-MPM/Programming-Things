### Una pequeña implementacion de matrices ###

def dimensiones(m1):
	row = len(m1)
	column = len(m1[0])
	return (row, column)

def zerosM(r, c):
	M = []
	R = []
	for i in range(0, r):
		R.append(0)
	for j in range(0, c):
		M.append(R)
	return M

def multEscalar(l, s):
	d = dimensiones(l)
	
	# Aqui definimos el ciclo para los renglones #
	i = 0
	while i < d[0]:
		# Aqui definimos el ciclo para las columnas #
		j = 0
		while j < d[1]:
			l[i][j] = s*l[i][j]
			j = j + 1
		i = i + j

	return l
'''
def mulMatrices(m1, m2):
	d1, d2 = dimensiones(m1), dimenciones(m2);
	if d1[1 == 2]
'''

def sumaMatrices(m1, m2):
	d1, d2 = dimensiones(m1), dimensiones(m2)
	
	if d1 == d2:
		maux = m1

		# Aqui definimos el ciclo para los renglones
		i = 0

		while i < d1[0]:
			# Aqui definimos el ciclo para las columnas #
			j = 0
			while j < d1[1]:
				maux[i][j] = m1[i][j] + m2[i][j]
				j = j + 1
			i = i + 1
		return maux
	else:
		print("No coincide la dimension")

def multMatrices(m1, m2):
	d1, d2 = dimensiones(m1), dimensiones(m2)
	c = zerosM(d1[0], d2[1])
	if d1[1] == d2[0]:
		i = 0
		while i < d1[0]:
			j = 0
			while j < d2[1]:
				aux = 0
				k = 0
				while k < d1[1]:
					aux = aux + m1[i][k]*m2[k][j]
					k = k + 1
				c[i][j] = aux
				j = j + 1
			i = i + 1
		return c

a = [[1, 2], [3, 4], [5, 6]]

print("La matriz inicial:" ,a)

#print("La multiplicacion escalar de Chio ", multEscalarChio(a, 2))


#print("La multiplicacion escalar de Pedro",multEscalar(a, 0.5))


print("La suma de matrices ", sumaMatrices(a, a))

print("Crea matriz de n por m", zerosM(4,2))

A = [[1, 2], [3, 4]]
I = [[1, 0], [0, 1]]
C = multMatrices(A, I)
print("La multiplicacion de ", A, " por ", I, " es ", C)
