import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def pca_plot(m):
    return list_plot(m.columns(), aspect_ratio=1)

df = pd.read_csv('https://raw.githubusercontent.com/davidaustinm/ula_modules/master/data/pca-demo.csv', index_col=0)	      
A = matrix([vector(row) for row in df.values]).T

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.scatter(df['0'], df['1'], df['2'])                                
plt.show()
