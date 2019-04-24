'''
n = int(input(" "))
'''
'''
numero fatorail é ele vezes 1,2,3,4,5=120
'''
'''
fat = 1
for i in range (2, n+1): #guardamos cada valor da multiplicação na variavel
                        #para multiplicar simultanemente
    fat = fat * i
print(fat)
'''
'''
'''
n = int(input(''))
div = 0 
for divi in range (1, n+1):
    if n % divi == 0:
        div += 1
if div == 2:
    print('primo')
else:
    print ('nao primo')