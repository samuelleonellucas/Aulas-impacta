from math import sqrt 
#importar raiz quadrada
xa= float(input())
ya= float(input())
xb= float(input())
yb= float(input())
xc= float(input())
yc= float (input())
dist_x = xa-xb
dist_y = ya-yb
dist_c = xc-xa

res = dist_x-dist_y
res1 = dist_y-dist_c
res2 = dist_c - dist_x


#a2 = sqrt(b2 + c2)
#square root(raiz quadrada)

dist_12 = sqrt (res**2 + res1**2 + res2**2)
print ('A-B: ' '%.2f' % res)
print ('B-C: ' '%.2f' % res1 )
print ('C-A: ' '%.2f' % res2 )
