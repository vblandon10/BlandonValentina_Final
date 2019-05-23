import matplotlib.pyplot as plt
import numpy as np

#Declaracion de las variables.

#tiempo en segundos
t=[3673,3628,3659,3652,3639,3737]
print(t)

#posiciones cartesianas en x (km)
px=[4,10,12,80,50,40]
print(px)

#posiciones cartesianas en x (km)
py=[100,5,80,50,50,200]
print(py)

def metropolis(t,px):
    actual=px
    MH=[]
    MH.append(actual)
    #array de pasos de MH
    for  i in range(N):
        propuesta=actual+np.random.normal()*500
        #propuesta
        p=min((t(i),propuesta)/(t(i),actual),1) #verosimilitud
        alpha=np.random.random()
        if(alpha < p):
            actual =  propuesta #se acepta el cambio
            MH.append(actual)
        else:
            MH.append(actual) #se rechaza el cambio
    return MH
    print (MH)
