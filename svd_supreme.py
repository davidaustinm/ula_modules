import numpy as np
import numpy.linalg as LA
import pandas as pd

def square(ll, dims, fillcolor, strokecolor):
    x, y = ll
    w, h = dims
    points = [ll, [x+w,y], [x+w, y+h], [x, y+h]]
    return polygon(points, rgbcolor=fillcolor, axes=False) + polygon(points,rgbcolor=strokecolor, fill=False,axes=False)

def display_column(A, k):
    w = copy(A.column(k))
    w /= np.max(np.abs(w))
    return display_matrix(matrix(w).T)

def display_matrix(A):
    max = np.max(A)
    min = np.min(A)
    scale = np.max([max, -min])
    squares=[]
    y = A.nrows()-1
    dim = 1
    for i, row in enumerate(A.rows()):
        x = 0
        for c in row:
            c /= scale
            if c > 1: c = 1
            fillcolor = [c]*3
            if c < 0: fillcolor=[-c,0,0]
            strokecolor = [1 - f for f in fillcolor]           
            squares.append(square([x,y], [dim,dim], fillcolor, strokecolor))
            x += dim
        y -= dim
    return sum(squares)

def plot_sv(A):
    sv = A.singular_values()
    return list_plot(sv, plotjoined=True) + list_plot(sv, size=30)

def outer(u, v):
    return matrix(u).T*matrix(v)

def approximate(A, k):
    A = np.array(A)
    u, s, vh = LA.svd(np.array(A))
    sigma = np.zeros(A.shape)
    r = np.min([k, len(s)])
    sigma[:r, :r] = np.diag(s[:r])
    return matrix(u.dot(sigma.dot(vh)))


cases = pd.read_csv('https://raw.githubusercontent.com/davidaustinm/ula_modules/master/data/Rehnquist-cases.csv', index_col=0)
fivefour = pd.read_csv('https://raw.githubusercontent.com/davidaustinm/ula_modules/master/data/Rehnquist-five-four.csv', index_col=0)
agreement = pd.read_csv('https://raw.githubusercontent.com/davidaustinm/ula_modules/master/data/rehnquist-agreement.csv', index_col=0)


