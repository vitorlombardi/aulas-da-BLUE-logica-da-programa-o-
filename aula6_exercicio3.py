custo =float(input('qual o valor do produto :' ) )

inposto =float(input('qual o valor do inposto : '))

def soma (custo,inposto):
    total = custo + ((inposto/100)*custo)
    print('o valor do produto é :', total)

soma(custo,inposto)



