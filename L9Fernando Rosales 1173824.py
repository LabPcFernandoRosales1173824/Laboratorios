print("Ejercicio 1: operaciones ariteméticas")

n1 = int(input("Ingrese el preimer número: "))
n2 = int(input("Ingrese el segundo número: "))

DivReal= n1/n2
DivEntera= n1//n2
DivModular= n1%n2
suma = n1+n2
resta = n1-n2
multi = n1*n2

print(n1,"+",n2,"=",suma)
print(n1,"-",n2,"=",resta)
print(n1,"*",n2,"=",multi)
print(n1,"/",n2,"=",DivReal)
print(n1,"//",n2,"=",DivEntera)
print(n1,"%",n2,"=",DivModular)

print("Ejercicio 2: operaciones booleanas")

igualdad = n1 == n2
diferentes = n1 != n2
mayor = n1>n2
menor = n1<n2

print(n1,">",n2,"=",mayor)
print(n1,"<",n2,"=",menor)
print(n1,"==",n2,"=",igualdad)
print(n1,"!=",n2,"=",diferentes)

print("Ejercicio 3: jerarquía de operadores")

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
c = int(input("Ingrese el tercer numero: "))

print("i. ",a*b+c)
print("ii. ",a*(b+c))
print("iii. ",a/(b+c))
print("iv. ",(3*a+2*b)/(c**2))

print("Actividad 3, Ejercicio 1")
m1 = int(input("Ingrese metros: "))

Km = m1/1000
Mill = Km/1.609
Ft = m1*3.28
Pul = Ft*12

print("Kilometros:",Km)
print("Millas:",Mill)
print("Pies:", Ft)
print("Pulgadas:", Pul)

print("Actividad 3, Ejercicio 2")

m2 = float(input("Ingrese metros: "))
Y = m2 // 0.9144
Mody = m2 % 0.9144
Pies = Mody // 0.333333
Pulgadas = m2 * 39.37

print ("Yardas: ", Y, "Pies: ",Pies,"Pulgadas:",Pulgadas)
