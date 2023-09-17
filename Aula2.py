"""
Operadores
"""
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

#assing
a = 10
a = a + 1
#mesma coisa que
a += 1
a -= 1
a *= 2
a **= 2

print(a)

#comparadores
a = 10

if(a == 10):
    a = 10000
    a =a + b
    
if(a != 10):
    a= 3

if( a> 10):
    a = 1

if(a >= 10):
    a = 1

if( a < 10):
    a = 1

if(a<= 5):
    a = 1

greco_calvo = True

if(not greco_calvo):
    print("carinho na cabeça")

a = [10,2,3,451,3,31,323,3]

if(8 not in a):
    print("10 existe")





