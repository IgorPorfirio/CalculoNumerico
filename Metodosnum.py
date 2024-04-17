#!/usr/bin/env python
# coding: utf-8

# In[156]:


import math

def f(x):
    return math.exp(x) - 2*x - 2.3

def df(x):
    return math.exp(x) - 2

def g1(x):
    return math.log(2*x+2.3)

def g2(x):
    return (math.exp(x) - 2.3) / 2


# In[157]:


def ponto_fixo(g, x0, precisao, iteracao_limite):
    x = x0
    
    for i in range(iteracao_limite):
        x_k = g(x)
        print(f"Iteração {i}:\n x = {x}; g(x) = {x_k}\n")

        if abs(x_k - x) < precisao:  # Condição de parada
            print(f"Convergiu após {i} iterações.")
            return x_k
        x = x_k
    print(f"Não converge em {iteracao_limite} iterações.")
    return x


# In[158]:


def bisseccao(f, a, b, precisao, iteracao_limite):
    if f(a) * f(b) >= 0:
        print("A função deve ter sinais opostos em a e b.")
        return None

    c = 0
    for i in range(iteracao_limite):
        # Ponto médio
        c = (a + b) / 2
        print(f"Iteração {i}:\n a = {a}; b = {b};\n Estimativa = {c}\n")
        # critérios de parada
        if f(c) == 0 or (b - a) / 2 < precisao:
            print(f"Convergiu após {i} iterações.")
            return c
        # encontrando intervalo com raiz: [a, c] ou [c, b]
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return c


# In[159]:


def falsa_posicao(f, a, b, precisao, iteracao_limite):
    if f(a) * f(b) >= 0:
        print("A função deve ter sinais opostos em a e b.")
        return None

    c = 0
    for i in range(iteracao_limite):
        # Ponto falsa posicao
        fa, fb = f(a), f(b)
        
        c = (a * fb - b * fa) / (fb - fa)

        
        print(f"Iteração {i}:\n a = {a}; b = {b};\n Estimativa = {c}\n")
        
        # Checando critérios de parada
        if f(c) == 0 or abs(c) < precisao:
            print(f"Convergiu após {i} iterações.")
            return c
        
        # encontrando intervalo com raiz: [a, c] ou [c, b]
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return c


# In[160]:


def secante(f, x0, x1, precisao, iteracao_limite):
    
    print(f"Iteração 0:\n x = {x0}; f(x) = {f(x0)}\n")
    print(f"Iteração 1:\n x = {x1}; f(x) = {f(x1)}\n")
    
    for i in range(iteracao_limite):
        
        fx0 = f(x0)
        fx1 = f(x1)
        
        
        if fx1 - fx0 == 0:
            print("Divisão por zero.")
            return None
        
        # Calcular o próximo x
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        
        print(f"Iteração {i+2}:\n x = {x2}; f(x) = {f(x2)}\n")

        
        # Checa a convergência
        if abs(x2 - x1) < precisao:
            print(f"Convergiu após {i+2} iterações.")
            return x2
        
        # Atualiza x0 e x1 para as próximas iterações
        x0, x1 = x1, x2
    
    print(f"Não converge em {iteracao_limite} iterações.")
    return x2 


# In[161]:


def newton_Raphson(f, df, x0, precisao, iteracao_limite):
    xn = x0
    for i in range(iteracao_limite):
        fxn = f(xn)
        print(f"Iteração {i}:\n x = {xn}; f(x) = {fxn}\n")

        if abs(fxn) < precisao:
            print(f"Raiz encontrada após {i} iterações.")
            return xn
        
        dfxn = df(xn)
        
        if dfxn == 0:
            print("Derivada zero. Nenhuma solução encontrada.")
            return None
        xn = xn - fxn / dfxn
        
    print(f"Não converge em {iteracao_limite} iterações.")
    
    return xn


# In[162]:


x = ponto_fixo(g1,1,pow(10,-20),50)
print(f"\nX = {x}; f({x}) = {f(x)}")


# In[163]:


x = ponto_fixo(g2,-1,pow(10,-20),100)
print(f"\nX = {x}; f({x}) = {f(x)}")


# In[164]:


x = bisseccao(f,-1,0,pow(10,-20),100)
print(f"\nX = {x}; f({x}) = {f(x)}")


# In[165]:


x = bisseccao(f,1,2,pow(10,-20),100)
print(f"\nX = {x}; f({x}) = {f(x)}")


# In[166]:


x = falsa_posicao(f,-1,0,pow(10,-20),1000)
print(f"\nX = {x}; f({x}) = {f(x)}")


# In[167]:


x = falsa_posicao(f,1,2,pow(10,-20),100)
print(f"\nX = {x}; f({x}) = {f(x)}")


# In[168]:


x = secante(f, -1, 0, pow(10,-20), 50)
print(f"\nX = {x}; f({x}) = {f(x)}")


# In[169]:


x = secante(f, 1, 2, pow(10,-20), 50)
print(f"\nX = {x}; f({x}) = {f(x)}")


# In[170]:


x = newton_Raphson(f, df, -1, pow(10,-20), 50)
print(f"\nX = {x}; f({x}) = {f(x)}")


# In[171]:


x = newton_Raphson(f, df, 1, pow(10,-20), 50)
print(f"\nX = {x}; f({x}) = {f(x)}")

