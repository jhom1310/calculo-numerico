def f(x):
    return x*x*x - 9*x + 5

def secante(a,b):
    
    if (f(a) * f(b) <= 0):
        i=0
        while True:
            if f(b) == f(a):
                print('Divisão por ZERO!')
                break

            c = b - (a-b)*f(b)/( f(a) - f(b) ) 
            print('Iteração-%d, raiz = %0.4f e f(raiz) = %0.4f' % (i, c, f(c)))
            b = round(a, 4)
            a = round(c,4)
            i += 1
            if (abs(f(c)) <= 0.01):
                break
            # Verifica se o ponto encontrado é raiz
            if (f(c) == 0.0):
                break     
        print("O valor da raiz é aproximadamente: : ","%.4f"%c)
        print("O valor da f(raiz) é aproximadamente: : ","%.4f"%f(c))
        print("Iterações: : ","%d"%i)
    else:
        print("Não existe raiz nesse intervalo\n")


a = float(input('informe o valor de A: '))
b = float(input('informe o valor de B: '))
secante(a, b)
