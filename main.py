import math
a = int(input("inserte el primer numero (a) porfavor:"))
b = int(input("inserte el segundo numero (b) porfavor:"))
c = int(input("inserte el tercer numero (c) porfavor:"))
d =math.sqrt((b**2)-(4*a*c))
x_pos = (-b + d)/(2 * a)
x_neg = (-b - d)/(2 * a)
cu_0 = -b/(2*a)
if d > 0:
 print ("La parte negativa es:"+ str(x_pos))
 print ("La parte positiva es:"+ str(x_neg))
if d == 0:
  print ("la solucion es:"+ str(cu_0))
if d < 0:
 print ("No existe solución en los números reales")
