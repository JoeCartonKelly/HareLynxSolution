# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 11:48:44 2022

@author: joeca
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("hare_lynx.csv")

a = 55
b = 55
c = 0.6
d = 900
data["hare estimate"] = a + b*np.sin(c*data["year"] + d)
data.plot(x="year", y=["hare", "hare estimate"])

N = len(data["year"])
error = 0.
for i in range(N):
    error += (data["hare"][i]-data["hare estimate"][i])**2
    
error /= N
print("The mean squared error is: ", error)

error = (1/N)*np.sum((data["hare"]-data["hare estimate"])**2)
print("The mean squared error is: ", error)