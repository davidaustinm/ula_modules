import pandas as pd
import numpy as np
from operator import itemgetter
from sage.plot.colors import rainbow

df = pd.read_csv("https://raw.githubusercontent.com/davidaustinm/ula_modules/master/data/clusters_data.csv", header = None)
data = [vector(r) for r in df.values]

def kmeans(data, k):
    N = 15
    centroids = sample(data, k)
    for _ in range(N):
        clusters = [ [] for __ in range(k)]
        for datum in data:
            distances = [(datum - centroids[j]).norm() for j in range(k)]
            clusters[np.argmin(distances)].append(datum)
        centroids = [mean(clusters[j]) if len(clusters[j]) > 0 else centroids[j] for j in range(k)]
    distances = [sum([(clusters[i][j] - centroids[i]).norm()**2
                      for j in range(len(clusters[i]))])
                     for i in range(len(clusters))]
    return [clusters, centroids, sum(distances)/len(data)]

def minimalobjective(data, k):
    results = [kmeans(data, k) for _ in range(10)]
    results = sorted(results, key=itemgetter(2))
    return results[0]

def plotclusters(clusters, centroids):
    k = len(clusters)
    colors = rainbow(k)
    plot = sum([list_plot(clusters[i], color=colors[i], size=20, aspect_ratio=1) for i in range(k)])
    return plot + list_plot(centroids, color='black', size=50)

