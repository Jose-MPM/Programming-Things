
class Alumno:
   
    def descripcion(self):
        print(f"{self.nombre} estudia en la {self.escuela}!")

    def __init__(self, n, e):
        self.nombre = n
        self.escuela = e
    
''' La forma de declarar un nuevo objeto de esta clase
    utilizando el inicializador '''
pedro = Alumno('Pedro', 'Falcultad de Ciencias')
# Mandamos a llamar el metodo descripcion.
pedro.descripcion()

