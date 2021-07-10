def func(x):
    print('x é', x )
    x=2
    print("valor local de x para : ",x )
x=50
func (x)
print('x ainda é : ',x )    

print()

def fun():
    global x 
    x=3
    y=x*2
    print(f'x global dentro da funçao = {x}')
    print(f'y global dentro da funçao = {y}')

print('inicio do programa')
x=20
print(f'o x global fora da funçao = {x}')
fun()
print(f'x global alterado dentro da funçao = {x}')

print()

def maior(x,y):
    if x>y:
      return x
    else:
      return y

print(maior(5,6))
