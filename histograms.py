# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 14:42:57 2022

@author: ddesa
"""

from pathlib import Path 
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from cell_analysis_tools.metrics import h_index
from sklearn.mixture import GaussianMixture

all_df = pd.read_csv(r"Z:\Danielle\Murphy iPSC CM\Exp 5 - hi v lo diff (1P)\histograms_screen5.csv")
#                         header=0,
#                         usecols=["Differentiation efficiency","norm_ORR_norm"])
# high_df = all_df[all_df["Differentiation efficiency"] == 'High']
# low_df = all_df[all_df["Differentiation efficiency"] == 'Low']
# h_array = high_df['norm_ORR_norm'].to_numpy()
# l_array = low_df['norm_ORR_norm'].to_numpy()
# listy = [h_array, l_array]
# y_variables = [
        # 'nadh_intensity_mean',
        # "nadh_tau_mean_mean",
        # "nadh_a2_mean",
        # "nadh_t1_mean",
        # "nadh_t2_mean",
        # 'fad_intensity_mean',
        # "fad_tau_mean_mean",
        # "fad_a1_mean",
        # "fad_t1_mean",
        # "fad_t2_mean",
        # "redox_ratio_mean",
        # "redox_ratio_norm_mean",
        # "norm_ORR_norm",
        #"area",
        #"flirr_mean",
        #"eccentricity",
    # ]

g=sns.histplot(data=all_df, x="ORR - Day 8", 
               hue="Efficiency", 
               kde=True, 
               palette="seismic",
               bins=25, 
               legend=True, 
               multiple="stack", 
               #element="step"
               )
sns.move_legend(g,loc="upper left", bbox_to_anchor=(1, 1))
plt.xlabel('Matrigel-normalized ORR')
plt.ylabel('Number of gels')
# sns.kdeplot(data=all_df, x="norm_ORR_norm", hue="day", palette="viridis")
# print(h_index([h_array]))
# print(h_index([l_array]))
