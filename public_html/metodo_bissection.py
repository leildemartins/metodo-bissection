'''
Olá Mundo!! esse é o básico do codigo
Solução aproximada da função f(x)=0 no intervalo [a,b] usando o método da bisseção.
Explicando termo a termo.

----------
f : função ------- A função que pretendemos achar a solução f(x)=0.

a,b : intervalo -- O intervalo que pretendemos achar a solução. 
                   A função retorna (None) caso f(a)*f(b) >= 0 

    N : (positivo) inteiro -- O número de interações.
 ----------
x_N :   O ponto médio considerando Nth intervarlo determinado pelo cálculo.
        O intervalo inicial [a_0,b_0] é dado por  [a,b].

''' 

# Inicio o programa definindo a função
def bissecao(f,a,b,N): 
    if f(a)*f(b) >= 0:
        print("Método da Bisseção falhou.")
        return None
    a_n = a
    b_n = b
    for n in range(1,N+1):
        m_n = (a_n + b_n)/2
        f_m_n = f(m_n)
        if f(a_n)*f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            print("Solução Exata.")
            return m_n
        else:
            print("Método da Bisseção falhou.")
            return None
    return (a_n + b_n)/2
"""
 Até esse parte do código é feita
 o calculo de bisseção

""" 

# Defino a função
f = lambda x: x**2-9

# Exibe o resultado do cálculo
approx = bissecao(f,2,4,10)
print(approx)

