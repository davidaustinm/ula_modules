import pandas as pd
import numpy as np

def degrees(x):
    return N(x*180.0/pi)

def demean(v):
    return vector(v - mean(v)*np.ones(len(v)))

def series_plot(v, color):
    return list_plot(v, color=color, plotjoined=True) + list_plot(v, color=color,size=20)

events = pd.read_csv("http://merganser.math.gvsu.edu/david/linear.algebra/ula/data/events.csv")
series = pd.read_csv("http://merganser.math.gvsu.edu/david/linear.algebra/ula/data/time-series.csv", header=None)

veterans = vector(events['Veterans Day'])
memorial = vector(events['Memorial Day'])
labor = vector(events['Labor Day'])
golden = vector(events['Golden Globe Awards'])
super = vector(events['Super Bowl'])

s1 = vector(series[0])
s2 = vector(series[3])
s3 = vector(series[1])
s4 = vector(series[2])



