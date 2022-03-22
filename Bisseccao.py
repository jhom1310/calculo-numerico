#import matplotlib.pyplot

def bisection(a,b,e):
    f = lambda x : eval(e)
    
    if (f(a) * f(b) >= 0):
        print("Não existe raiz nesse intervalo\n")
        return
  
    c = a
    while ((b-a) >= 0.01):
        # Encontra o ponto médio
        c = (a+b)/2 
        # Verifica se o ponto médio é raiz
        if (f(c) == 0.0):
            break
        # Decide o lado para repetir os passos
        if (f(c)*f(a) < 0):
            b = c
        else:
            a = c           
    print("O valor da raiz é apriximadamente: : ","%.4f"%c)


a = float(input('informe o valor de A: '))
b = float(input('informe o valor de B: '))
e = input('informe a expressão: ')
bisection(a, b, e)


