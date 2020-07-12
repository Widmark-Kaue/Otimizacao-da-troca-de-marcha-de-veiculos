# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 11:03:26 2019

@author: Widmark Kauê
"""
import numpy as np
import matplotlib.pylab as plt
from numpy.linalg import solve

def spl3System(xp,fp):
    n1 = xp.shape
    n2 = fp.shape
    assert n1 == n2, "spl3System: x e y não possuem o mesmo número de elementos"
    n =  len (xp) - 1
    Asys = np.zeros ([n+1,n+1])
    bsys = np.zeros(n+1)
    Asys[0,0] = 1
    Asys[-1,-1] = 1
    
    for i in range(1,n):
        ##Montando matriz de coeficientes para resolver C
        Asys[i,i-1] = xp[i] - xp[i-1]                
        Asys[i,i+1] = xp[i+1] - xp[i]                
        Asys[i,i]   = 2*(Asys[i,i-1] + Asys[i,i+1])
        ##Montando matriz dos termos independentes para resolver C
        dd1 = (fp[i+1] - fp[i])/(xp[i+1] - xp[i])
        dd0 = (fp[i] - fp[i-1])/(xp[i] - xp[i-1])
        bsys[i] = 3*(dd1 - dd0)
    return Asys, bsys

def spl3Coeff(xp,fp):
    Asys, bsys = spl3System(xp,fp)
    #Resolver coeficiente c
    c = solve (Asys,bsys)
    ###Resolvendo b e d em relação a C
    n =  len (xp) - 1
    a = np.zeros(n)
    b = np.zeros(n)
    d = np.zeros(n)
    for i in range  (0,n):
        ###Assume que o termo indepente da função cúbica é a imagem da função no intervalo i   
        a[i] = fp[i] 
        h = xp[i+1] - xp[i]
        d[i] = (c[i+1] - c[i])/(3*h) #resolução de d
        dd1 = (fp[i+1] - fp[i])/(xp[i+1] - xp[i])
        b[i] = dd1 - (1/3)*(c[i+1] + 2*c[i])*h
    return a, b, c, d

def spl3EvalS(a, b, c, d, xp, z):
    ##Verifica se o ponto x está dentro do intervalo de interpolação
        assert (z >= xp[0]) and (z <= xp[-1]) ,"spl3EvalS: O ponto está fora do intervalo de interpolação"
        
        ####Verifica em qual intervalo está x
        i = 0
        while ( z > xp[i+1] ):
            i = i + 1
        
        ##Monta a função cúbica de acordo com os seus coeficientes
        s = a[i] + b[i]*(z - xp[i]) + c[i]*(z - xp[i])**2 + d[i]*(z - xp[i])**3  
        
        return s
  


    
    
    
    
    
    