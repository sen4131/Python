# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 18:14:40 2018

@author: Sen
"""
import pandas
import numpy as np
import matplotlib.pyplot as plt

#dataframe
df = pandas.read_csv('C:/Users/Sen/Downloads/CUS 615 (DM II)/Lab/Lab2/IRIS.csv')

#Summary stat
df.shape 
round(df.describe(),3)

#1.2 Data Vizualization
def graph(df):
    names = df.head(0)    
    for i in names:
        try:
            #1 All histograms
            print('Hist of '+i)
            plt.hist(eval('df.'+i))
            plt.show()
            #2 All Box plots
            print('Boxplot of '+i)
            plt.boxplot(eval('df.'+i))
            plt.show() 
        except:
            continue
        
graph(df)

#Question 2
df = pandas.read_csv('C:/Users/Sen/Downloads/CUS 615 (DM II)/Lab/Lab2/pendigits.csv')
df.shape 
round(df.describe(),3)
graph(df)

#Q3



