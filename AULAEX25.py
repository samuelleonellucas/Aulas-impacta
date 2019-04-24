'''
num = float(input(" "))
if 1 <= num and num <= 100:
    print("dentro do intervalo")

num = float(input(" "))

if 30 < num and num <70:
    print("dentro do intervalo")
else:
    print ("fora do intervalo")
'''
'''
num1 = int(input( ))
num2 = int(input( ))
num3 = int(input( ))

if num1 < num2 < num3:

    print(num1, "num1")

elif num2 > num1 <num3:

    print (num2, "num2")
else:
    print(num3, "num3")
    '''
'''
a = int(input("a "))
b = int(input("b "))
c = int(input("c "))

if a < b and a < c :
    print(a, "a")
    if b < c:
        print(b, "b")
        print(c, "c")
    else:
        print (c, "c")
        print (b, "b")
elif b < a and b < c:
    print(b, "b")
    if a < c:
        print (a, "a")
        print (c, "c")
    else:
        print (c, "c")
        print (a, "a")
        if a < b:
            print (b, "b")
            print (a, "a")
'''


''''
soma = 0
while True:
     num1 = int(input(' '))
     soma = soma + num1
     if num1 == 0:
         break
     print (soma)


'
''
num1 = int(input())

soma = 0
while num1 != 0:
    soma = soma + num1
    num1 = int(input(' '))
    print (soma)
'''
   
'''
while True:
    sal = int(input('quantidade'))
    if sal > 0:
        break
    else:
        print ('Quantidade inválida')
soma = 0
for cont in range (sal):
    salario = float(input('salario'))
    soma += sal
print (soma )
''' 