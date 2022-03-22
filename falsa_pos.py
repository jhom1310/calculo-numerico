#import matplotlib.pyplot
MAX_ITERACOES = 100000
def falsa_pos(a,b,e):
    f = lambda x : eval(e)
    
    if (f(a) * f(b) <= 0):
        
        c = a
        for i in range(MAX_ITERACOES):
            
            c = (a * f(b) - b * f(a)) / (f(b) - f(a))
            # Verifica se o ponto encontrado é raiz
            if (f(c) == 0.0):
                break
            # Decide o lado para repetir os passos
            if (f(c)*f(a) < 0):
                b = c
            else:
                a = c           

            print(i)
        print("O valor da raiz é apriximadamente: : ","%.4f"%c)
    else:
        print("Não existe raiz nesse intervalo\n")


a = float(input('informe o valor de A: '))
b = float(input('informe o valor de B: '))
e = input('informe a expressão: ')
falsa_pos(a, b, e)


''