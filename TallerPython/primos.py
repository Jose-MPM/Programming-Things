#linea que nos permite leer entero en nuestra terminal
n = int(input("Ingrese un número natural: "))

## Funcion que recibe un numero y te dice si este es un numero primo o no ##
def primo(n):
	i = 2
	a = True
	while i < n:
		if n%i == 0:
			a = False
			i = n
		else:
			i = i+1
	return a

### Funcion que crea una lista con los numeros primos que existan entre el 2 y el numero que introduce el usuario ###
def primos(n):
	primes = []

	for i in range(2, n):
		if primo(i):
			primes.append(i)

	return primes

#### Funcion que crea una lista con pares de numeros primos gemelos entre el 0 y el numero que introduce el usuario ####
def gemelos(n):
	primosGemelos = []
	l = primos(n)
	i = 1
	while i < len(l):
		if l[i] - l[i - 1] == 2:
			primosGemelos.append( (l[i-1], l[i]) )
		i = 1 + i
	return primosGemelos

# #




print(primo(n))

print(primos(n))

print(gemelos(n))
