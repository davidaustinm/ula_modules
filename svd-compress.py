from PIL import Image
import numpy as np
import numpy.linalg as LA
import pandas as pd
import requests
from io import BytesIO

def display_image(matrix):
    matrix = np.array(matrix)
    matrix = np.maximum(0, matrix)
    matrix = np.minimum(255, matrix)
    return Image.fromarray(matrix.astype('uint8'))

def approximate(A, k):
    A = np.array(A)
    u, s, vh = LA.svd(np.array(A))
    sigma = np.zeros(A.shape)
    r = np.min([k, len(s)])
    sigma[:r, :r] = np.diag(s[:r])
    return matrix(u.dot(sigma.dot(vh)))


'''    
    U, S, V = matrix(RDF, A).SVD()
    krange = range(k)
    U = U.matrix_from_columns(krange)
    S = S.matrix_from_rows_and_columns(krange, krange)
    V = V.matrix_from_columns(krange)
    return U*S*V.T
'''

def square(ll, dims, fillcolor, strokecolor):
    x, y = ll
    w, h = dims
    points = [ll, [x+w,y], [x+w, y+h], [x, y+h]]
    return polygon(points, rgbcolor=fillcolor, axes=False) + polygon(points,rgbcolor=strokecolor, fill=False,axes=False)

def display_vector(v):
    w = copy(v)
    w /= np.max(np.abs(v))
    return display_matrix(matrix(w).T)

def display_matrix(A):
    squares=[]
    y = A.nrows()-1
    for i, row in enumerate(A.rows()):
        x = 0
        for c in row:
            if c > 1: c = 1
            fillcolor = [c]*3
            if c < 0: fillcolor=[-c,0,0]
            strokecolor = [1 - f for f in fillcolor]           
            squares.append(square([x,y], [1,1], fillcolor, strokecolor))
            x += 1
        y -= 1
    return sum(squares)

def plot_sv(A):
    sv = A.singular_values()
    return list_plot(sv, plotjoined=True) + list_plot(sv, size=30)

url = 'http://merganser.math.gvsu.edu/david/linear.algebra/ula/data/utah-gray.png'
response = requests.get(url)
image = Image.open(BytesIO(response.content)).convert('LA')
image = np.array(image)[:,:,0]
image = np.array(image)

noise = pd.read_csv('http://merganser.math.gvsu.edu/david/linear.algebra/ula/data/noise.csv', header=None, index_col=False)


letter = pd.read_csv('http://merganser.math.gvsu.edu/david/linear.algebra/ula/data/letter.csv', header=None, index_col=False, sep=' ')
A = matrix(RDF, letter.values)

url = 'http://merganser.math.gvsu.edu/david/linear.algebra/ula/data/new-utah-noise.png'
response = requests.get(url)
noiseimage = Image.open(BytesIO(response.content)).convert('LA')
noiseimage = np.array(noiseimage)[:,:,0]
noiseimage = np.array(noiseimage)



