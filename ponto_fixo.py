def f(x):
    return x*x*x - 9*x + 5

def fi(x):
    #(x.^3+5)/9;
    return (x**3 + 5) / 9

def ponto_fixo(a,b):
    
    if (f(a) * f(b) <= 0):
        i=0
        c = (a + b)/2
        while (abs(f(c)) >= 0.01):
            c = fi(c)
            c = round(c,4)
            print('Iteração-%d, raiz = %0.4f e f(raiz) = %0.4f' % (i, c, f(c)))           
            i += 1
            # Verifica se o ponto encontrado é raiz
            if (f(c) == 0.0):
                break         
        print("#"*50)    
        print("O valor da raiz é aproximadamente: : ","%.4f"%c)
        print("O valor da f(raiz) é aproximadamente: : ","%.4f"%f(c))
        print("Iterações: : ","%d"%i)
    else:
        print("Não existe raiz nesse intervalo\n")


a = float(input('informe o valor de A: '))
b = float(input('informe o valor de B: '))
ponto_fixo(a, b)
