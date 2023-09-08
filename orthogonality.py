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
    return vector(v - np.mean(v.coefficients())*onesvec(len(v)))

def vandermonde(data, k):
    rows = [[datum**j for j in range(k+1)] for datum in data]
    return matrix(rows)

def plot_model(xhat, data, domain = None):
    xmax = data[0][0]
    xmin = data[0][1]
    k = len(xhat)-1
    for d in data:
        if d[0] > xmax: xmax = d[0]
        if d[0] < xmin: xmin = d[0]
    if domain == None: domain = (xmin, xmax)
    return list_plot(data, size=40, color='blue') + plot(xhat*vector([x**j for j in range(k+1)]), (x, domain[0], domain[1]), color='red') 
    

