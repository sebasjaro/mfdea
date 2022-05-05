"""Main module."""

import numpy as np
from collections import Counter

def proba(xl):
   prob = Counter(xl).most_common()
   return(prob)

def entro(x):
   p = proba(x)
   lonx = len(x)
   lonp = len(p)
   pi = np.zeros(lonp)
   for i in range(lonp):
      pi[i] = (p[i][1])/lonx
   lpi = np.log(pi)
   return(-1. *  np.inner(pi,lpi))

test = np.random.randint(1,3,20)
test = np.array([1,1,-1,1,-1])
N = len(test)

ts = np.arange(1,6)

for t in ts:
    n_traje = N - t + 1  # numero de secuencias para cada t
    xs = np.zeros(n_traje, dtype=int)
    for s in range(n_traje):
        for i in range(t):
            xs[s] = xs[s] + test[i+s]
    print(t, entro(xs))

        

    
