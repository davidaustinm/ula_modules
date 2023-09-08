import numpy as np
import pandas as pd

def projection(b, basis):
    if len(basis) == 0: return vector([0] * len(b))
    return sum([ (b*v)/(v*v)*v for v in basis ])

def unit(v):
    return 1/v.norm() * v

def gs(basis):
    onbasis = []
    for b in basis:
        onbasis.append(unit(b - projection(b, onbasis)))
    return onbasis

def QR(A):
    Q = matrix(gs(A.columns())).T
    return Q, Q.T*A

def onesvec(n):
    return vector([1] * n)

def demean(v):
    return v - np.mean(v)*onesvec(len(v))

