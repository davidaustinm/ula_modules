import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def culmen_plot():
    fig = plt.figure()#figsize=(10,10))
    ax = fig.add_subplot('111')
    ax.set_aspect(1)
    sns.scatterplot(x = 'Culmen Length (mm)', y = 'Culmen Depth (mm)', hue = 'Species', style='Sex', data=df, ax=ax)
    plt.legend(bbox_to_anchor=(0,1.05), loc=3, borderaxespad=0.)
    plt.show()

def pca_plot(M, sex='all'):
    d = np.array([list(c) for c in M.columns()])
    proj = pd.DataFrame(d, columns=[0,1])
    proj['Species'] = df['Species']
    proj['Sex'] = df['Sex']
    fig = plt.figure()#figsize=(20,10))
    ax = fig.add_subplot('111')
    ax.set_aspect(1)
    if sex == 'all':
        sns.scatterplot(x = 0, y = 1, hue = 'Species', style='Sex', data=proj, ax=ax)
    if sex == 'male':
        proj = proj[proj['Sex'] == 'Male']
        sns.scatterplot(x = 0, y = 1, hue = 'Species', data=proj, ax=ax)
    if sex == 'female':
        proj = proj[proj['Sex'] == 'Female']
        sns.scatterplot(x = 0, y = 1, hue = 'Species', data=proj, ax=ax)
    plt.legend(bbox_to_anchor=(-.15,1.05), loc=2, borderaxespad=0.)
    plt.show()


df = pd.read_csv('https://raw.githubusercontent.com/davidaustinm/ula_modules/master/data/penguins.csv')
df = df.drop(columns=['Unnamed: 0'])
data = pd.read_csv('https://raw.githubusercontent.com/davidaustinm/ula_modules/master/data/penguins_data.csv')
data = data.drop(columns=['Unnamed: 0'])
A = matrix(data.values).T
