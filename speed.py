# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 15:11:33 2019

@author: Widmark Kauê
"""

import numpy as np
import spl3
import root
import matplotlib.pylab as plt

def gearShift(torque, w, ratio, R):
    """
    Retorna um vetor com as velocidade ideiais para a troca de marcha.

    Parameters
    ----------
    torque : Array
        Vetor de torques.
    w : Array
        Vetor de velocidade angular.
    ratio : Array
        Razão entre as marchas.
    R : Float
        Raio....

    Returns
    -------
    Trm : Array
        Vetor de velocidades ótimas para a troca de marcha.
    TT: Array
        Vetor de torques na velocidade ideal.

    """
    n1, = torque.shape
    n2, = w.shape
    n3, = ratio.shape
    assert n2 == n1, "gearShit: Os arrays torque e w possuem tamanhos distintos."
    T1 = np.zeros(n3) #vetor de funções do torque em relação a velocidade
    T2 = np.zeros(n3)
    Trm = np.zeros (n3 - 1) #vetor com velocidades ideiais para troca de marcha
    TT = np.zeros (n3 - 1) # vetor com torque na velocidade ideal
    v1 = (w*R)/ratio[0]
    a1, b1, c1, d1 = spl3.spl3Coeff(v1,torque)
    for i in range(n3-1):
        T1 = lambda x: spl3.spl3EvalS(a1, b1, c1, d1, v1, x)
        v2 = (w*R)/ratio[i+1]
        a, b, c, d = spl3.spl3Coeff(v2,torque)
        T2 = lambda x: spl3.spl3EvalS(a, b, c, d, v2, x)
        T = lambda x: T1(x) - T2(x)
        if (v1[0] <= v2[0]):
            if (v1[-1] >= v2[-1]):
                v = np.linspace(v2[0], v2[-1],20)
            else:
                v = np. v = np.linspace(v2[0], v1[-1],20)
        else:
            if (v1[-1] >= v2[-1]):
                v = np.linspace(v1[0], v2[-1],20)
            else:
                v = np. v = np.linspace(v1[0], v1[-1],20)
        n, trm = root.bissect(T,v[0],v[-1])
        TT[i] = T1(trm)
        Trm[i] = trm
        v1 = v2
        a1, b1, c1, d1 = a, b, c, d
    return Trm, TT

def plot (torque, w, ratio, R, gearShift = None):
    """
    Plotar um gráfico com as curvas de torque para cada marcha.

    Parameters
    ----------
    torque : Array
        Vetor de torques.
    w : Array
        Vetor de velocidade angular.
    ratio : Array
        Razão entre as marchas.
    R : Float
        Raio.

    Returns
    -------
    None.

    """
    plt.figure()
    n, = ratio.shape
    Wid = np.array(["1º marcha", "2º marcha","3º marcha","4º marcha","5º marcha","6º marcha"])
    for i in range (n):
        v = (w*R)/ratio[i]
        a, b, c, d = spl3.spl3Coeff(v,torque)
        xg = np.linspace(v[0],v[-1],200)
        N, = xg.shape
        yg = np.zeros(N)
        for j in range (N):
            yg[j] = spl3.spl3EvalS(a, b, c, d, v, xg[j])
        # plt.plot(v,torque, "o")
        plt.plot(xg,yg, label = Wid[i])
        
    if gearShift is not None:
        plt.plot(gearShift[0], gearShift[1], "ko")
        plt.annotate("Velocidade ideal", (gearShift[0][-1], gearShift[1][-1]), 
                     xytext=(gearShift[0][-1]  + 10, gearShift[1][-1] - 110), 
                     arrowprops=dict(facecolor='black', shrink=0.05, width=0.5, headwidth=4),
                     bbox=dict(facecolor='lightgray', boxstyle = 'round, pad=0.3'))
    plt.xlabel("Velocidade (m/s)")
    plt.ylabel("Torque (Nm)")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    # Dados para Ferrari 360 Modena
    # Raio
    R = 0.3385 # metros

    # Razão das marchas 
    ratio = np.array([ 14.59,   9.58,   7.14,   5.63,   4.59,   3.77])

    # Tabela de Dados velocidade de rotaçao (rad/s) vs torque (Nm)
    w      = np.array([ 104.7,  157. ,  209.4,  261.8,  314.15,  366.5 ,  418.9 , 471.2 ,  523.6 ,  
                       575.9 ,  628.3 ,  680.7 ,  733.  ,  785.4 , 837.7 ,  890.1 ,  942.5 ])
    torque = np.array([ 170.8,  256.2,  298.8,  324.5,   341.5,  353.7,   362.9,  370. ,   372.8 ,  
                       371.3 ,  368.3 ,  363.7 ,  357.6 ,  350.  ,  340.9,  330.3 ,  280.7 ]) 


    plot(torque, w, ratio, R, gearShift(torque, w, ratio, R))
    




    
        
    

