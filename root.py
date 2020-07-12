# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 15:04:11 2019

@author: Widmark Kauê
"""

def bissect(f,a,b,TOL=1E-5, NMAX = 100) :

    fa=f(a)
    fb=f(b)
    
    assert fa*fb<0,"bissect: A função deve ter sinais opostos nos extremos."
    assert b>a, "bissect: O extremo superior b deve ser maior que o extremo inferior a."
    
    n=1
    
    while(0.5*(b-a) > TOL):
        p=0.5*(b+a)
        fp=f(p)
        
        if (fp==0):
            return n,0,p
        
        if (fa*fp<0):
            b=p
            fb=fp
        else:
            a=p
            fa=fp
            
        n=n+1 
        assert n < NMAX, "bissect: Número máximo de passos atingido."           
    return n, 0.5*(b+a)