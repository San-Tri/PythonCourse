# definiendo una variables:
a = 5
b = 4.8
c = a + b
print(c)
# definiendo variables con snake_case
nombre_competo_siuuu = "spayderman"
# definiendo variables con camelCase
nombreCompetoSiuuu = "spayderman" 
# Declarar variable = definicion de varaible:
nombre = "jhon"
print(nombre)
# Otra forma de suma: 
d = 4 + 8
print(d)
# Las variables se puden redefinir:
nombre = "Pepe"
nombre = "Luis"
nombre = "Pedro"
print(nombre)
# redificion suma:
número = 10
número += 7
número -= 3
print(número)
# concantenar (unir palabras):
nombre = ' Lucas'
bienbenida = ' Hola' + nombre + " ¿Como estas?"
print(bienbenida)
# concatenar con "f-string":
nombre = True
bienbenida = f"hola {nombre} ¿como estas?"
print(bienbenida)
# dejar de declarar una variable, usar el "operador del":
nombre = True
bienbenida = f"hola {nombre} ¿como estas?"
del bienbenida
print(bienbenida)

nombre = True
del nombre
bienbenida = f"hola {nombre} ¿como estas?"
print(bienbenida)