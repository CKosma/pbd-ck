# -*- coding: utf-8 -*-
"""
Created on Sun May 24 10:39:07 2020

@author: CamilaKosma
"""

import numpy as np 
import pandas as pd 

from sklearn import preprocessing
from matplotlib import pyplot as plt 
import statsmodels.api as sm
import statsmodels.formula.api as smf

from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error

plt.show()
plt.rc("font", size=14)
import seaborn as sns
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)

	
df_red = pd.read_csv('https://query.data.world/s/73etlzoggogvvexdsftcc32spsbeuz')
df_white = pd.read_csv('https://query.data.world/s/hirjheciwp5tsqnd2jmvjpzhirwhfe')

print(df_red)
print(df_white)
    
df_red["colour"] = "R"
df_white["colour"] = "W"
df_all = pd.concat([df_red, df_white], axis = 0)
print(df_all)
df_all.head()
print(df_all.head())

df_white.rename(columns={'fixed acidity': 'fixed_acidity','citric acid':'citric_acid','volatile acidity':'volatile_acidity','residual sugar':'residual_sugar','free sulfur dioxide':'free_sulfur_dioxide','total sulfur dioxide':'total_sulfur_dioxide'}, inplace=True)
df_red.rename(columns={'fixed acidity': 'fixed_acidity','citric acid':'citric_acid','volatile acidity':'volatile_acidity','residual sugar':'residual_sugar','free sulfur dioxide':'free_sulfur_dioxide','total sulfur dioxide':'total_sulfur_dioxide'}, inplace=True)
df_all.rename(columns={'fixed acidity': 'fixed_acidity','citric acid':'citric_acid','volatile acidity':'volatile_acidity','residual sugar':'residual_sugar','free sulfur dioxide':'free_sulfur_dioxide','total sulfur dioxide':'total_sulfur_dioxide'}, inplace=True)

df = pd.get_dummies(df_all, columns=["colour"])

print(df_all.isnull().sum())
print(df_all.shape)
print(df_all.describe())

print("white wine mean = ",df_white["quality"].mean())
print("red wine mean =",df_red["quality"].mean())
d = {'colour': ['red','white'], 'mean_quality': [5.636022, 5.877909]}
df_mean = pd.DataFrame(data=d)
print(df_mean)

plt.subplots(figsize=(12,10))
ax = plt.axes()
ax.set_title("Wine Characteristic Correlation Heatmap (Reds)")
corr = df_red.corr()
sns.heatmap(corr, 
            xticklabels=corr.columns.values,
            yticklabels=corr.columns.values,
           cmap="Reds")
plt.show()

plt.subplots(figsize=(12,10))
ax = plt.axes()
ax.set_title("Wine Characteristic Correlation Heatmap (Whites)")
corr = df_white.corr()
sns.heatmap(corr, 
            xticklabels=corr.columns.values,
            yticklabels=corr.columns.values,
           cmap="Blues")
plt.show()

df_red_corr=df_red.corr()
df_white_corr=df_white.corr()

print(df_red_corr)
print(df_white_corr)

diff_corr = df_red_corr - df_white_corr
print(diff_corr)

plt.subplots(figsize=(12,10))
ax = plt.axes()
ax.set_title("Correlation Differences between Red and White Wines")
corr = diff_corr
sns.heatmap(corr, 
            xticklabels=corr.columns.values,
            yticklabels=corr.columns.values,
           cmap="coolwarm")
plt.show()





