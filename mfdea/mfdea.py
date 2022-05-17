import numpy as np
import matplotlib.pyplot as plt

def renyi(p,q):
   return np.log(np.sum(p**q))/(1-q)

def proba(x, size):
    #bins = int(len(x)/size)
    bins = (np.max(x)-np.min(x))/size
    h1, h2 = np.histogram(x, bins = int(bins))
    nozero = np.nonzero(h1)[0]
    p = [h1[w] for w in nozero]
    return np.array(p)

def dea(array, si, sf, file, n):
   N = len(array)
   ts = np.arange(si,sf,10)
   size = np.std(test)/n
   for t in ts:
       n_traje = N - t + 1
       xs = np.zeros(n_traje)
       xs = [np.sum(array[s:t+s]) for s in range(n_traje)]
       prob = proba(xs, size)/n_traje
       file.write(str(t) + ' ' + str(-1 * np.inner(prob,np.log(prob))) + ' ' + str(renyi(prob,5)) + '\n')



#np.random.seed(100)
#test = np.random.randint(1,3,1000)
#test = np.array([1,1,-1,1,-1,])
#test = np.loadtxt('./datos/walk_short_eco110k.gb')

from fbm import FBM 
f = FBM(n=50000, hurst=0.75, length=1, method='daviesharte')
test = f.fgn()

import pandas as pd
from scipy.stats.kde import gaussian_kde

N = len(test)
si = 1
sf = 300
valores = [.5,1,1.5,2,2.5,3,3.5,4,4.5,5]
for val in valores:
    file = open('salida_dea'+'_'+str(val)+'.dat','w')
    dea(test, si, sf, file, val)
    file.close()

