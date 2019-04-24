'''
from math import sqrt 
#importar raiz quadrada
xa= float(input())
ya= float(input())

xb= float(input())
yb= float(input())

xc= float(input())
yc= float(input())

dist_ab = sqrt((xb-xa)**2+(yb-ya)**2)
dist_bc = sqrt((xc-xb)**2+(yc-yb)**2)
dist_ca = sqrt((xa-xc)**2+(ya-yc)**2)


print ('A-B: %2f' % dist_ab)
print ('B-C: %2f' % dist_bc)
print ('C-A: %2f' % dist_ca)
'''

'''
n = float(input(' '))
m = int(input(' '))
pot = 1
for i in range(m):
    pot = pot * n
print (pot)

'''
'''
n = float(input(' '))
m = int(input(' '))
pot = 1


'''

n1 = int(input())
n2 = int(input())
mult = 0
while n2 < mult:
    mult = mult + n1
print (mult)


'''
n1 = int(input())
n2 = int(input())
vezes = 1
n1 = n1 + n1
while n2 < vezes:
    vezes = vezes + 1
print (n1)

'''