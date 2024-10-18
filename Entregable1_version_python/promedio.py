N=int(input("Ingrese el numero de libros que leyó: " ))
N1=int(input("Ingrese el tiempo en dias que demoro leyendo esa cantidad de libros: " ))
suma=0 # Aqui en esta variable se van a guardar la suma acumulada de lo que yo quiero promediar.
i=1
while(i<=N): # Con este ciclo while, se va a pedir el numero de las paginas que tenia cada libro
    print("Ingrese el numero de paginas del libro numero: ", i)
    paginas=int(input()) # Los valores de las paginas se guardan aqui, se pone int y no float ya que el numero de paginas no tiene decimales
    suma=suma+paginas
    i+=1 # Es la forma en que incrementamos la variable de control i, asi cuando i<=N como esta en el comienzo de nuestro ciclo while, entonces ya deja de pedirnos valores a poner en este caso teniendo en cuenta el numero de libros.
prom=suma/N1 # Aqui se promedia las paginas/dias de lectura para un promedio de paginas por dia
print("El promedio de paginas que leyó por dia es de: ", prom)
