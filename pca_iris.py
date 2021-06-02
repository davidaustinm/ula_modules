import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def sepal_plot():
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.set_aspect(1)
    sns.scatterplot(x = 'sepal length', y = 'sepal width', hue = 'species', style='species', data=df, ax=ax)
    plt.legend(bbox_to_anchor=(0,1.05), loc=3, borderaxespad=0.)
    plt.show()

def pca_plot(M):
    d = np.array([list(c) for c in M.columns()])
    proj = pd.DataFrame(d, columns=[0,1])
    proj['species'] = df['species']
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.set_aspect(1)
    sns.scatterplot(x = 0, y = 1, hue = 'species', style='species', data=proj, ax=ax)
    plt.legend(bbox_to_anchor=(0,1.05), loc=3, borderaxespad=0.)
    plt.show()


df = pd.read_csv('https://raw.githubusercontent.com/davidaustinm/ula_modules/master/data/iris.data')
data = df[df.columns[:4]]
data_mean = vector(data.mean())
A = matrix([vector(row) for row in (data-data.mean()).values]).T
df
