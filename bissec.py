def bisection(a,b,e):
    f = lambda x : eval(e)
    
    if (f(a) * f(b) <= 0):
        i = 0
        c = a
        while (abs(f(c)) >= 0.01):
            # Encontra o ponto médio
            c = (a+b)/2
            c = round(c,4)
            print('Iteração-%d, raiz = %0.4f e f(raiz) = %0.4f' % (i, c, f(c)))
            i += 1 
            # Verifica se o ponto médio é raiz
            if (f(c) == 0.0):
                break
            # Decide o lado para repetir os passos
            if (f(c)*f(a) < 0):
                b = c
            else:
                a = c       
        print("#"*50)            
        print("O valor da raiz é aproximadamente: : ","%.4f"%c)
        print("O valor da f(raiz) é aproximadamente: : ","%.4f"%f(c))
        print("Iterações: : ","%d"%i)
        
    else:
        print("Não existe raiz nesse intervalo\n")


a = float(input('informe o valor de A: '))
b = float(input('informe o valor de B: '))
e = input('informe a expressão: ')
bisection(a, b, e)


