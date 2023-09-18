"""
Operadores
"""

#Função criada por nós para simular ceiling
def ceil(x,y):
    if(x%y > 0):
        return (x//y)+1
    else:
        return x/y

a = 15
b = 7

#arithmetics
print("soma:",a + b)
print("sub: ",a- b)
print("mult: ",a*b)
print("div:",(a/b))
print("flor_div", (a//b))
print("ceil_div", ceil(a,b))
print("modulo:", a%13)
print("exp:", 2**a)

#tipos de assing
a = 10
a = a + 1
a += 1
#a = a+1 <-> a+=1
a -= 1 #<-> a = a-1
a *= 2 #<-> a = a*2
a **= 2 #<-> a = a**2
print(a)

#Operadores de Comparação
a = 10

#retorna TRUE se forem iguais
if(a == 10):
    a =a + b

#retorna TRUE se forem diferentes
if(a != 10):
    a= 3

#retorna ture se a for maior que 10
if( a> 10):
    a = 1

#retorna ture se a for maior ou igual a 10
if(a >= 10):
    a = 1

#retorna ture se a for menor que 10
if( a < 10):
    a = 1

#retorna ture se a for menor ou igual a 5
if(a<= 5):
    a = 1

greco_calvo = True

#not da lógica matemática
if(not greco_calvo):
    print("carinho na cabeça")


a = [10,2,3,451,3,31,323,3]
#procura se 8 está na lista a
if(8 not in a):
    print("10 existe")





