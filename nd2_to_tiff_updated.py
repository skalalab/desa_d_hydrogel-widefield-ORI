# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 09:17:03 2023

@author: ddesa
"""


import nd2
import tifffile
import pandas as pd
import os

CSV = "./Exp10_patterns_cell-map.csv"
filemap = pd.read_csv(CSV)
nd2_file = r'Z:\Danielle\Murphy iPSC CM\nd2\2023-12-06_patterns_day10.nd2'
images = nd2.imread(nd2_file)

for i in range(len(filemap)):
    path = os.path.join('./2023-12-06_Patterns/', filemap["Well"][i])
    if not os.path.exists(path):
        os.makedirs(path)

    name = f'{filemap["Well"][i]}_{filemap["Hydrogel"][i]}_{filemap["Date"][i]}_{filemap["Stiffness"][i]}_{filemap["Pattern"][i]}'
    NADH_path = os.path.join(path, name + "_N.tif")
    FAD_path = os.path.join(path, name + "_F.tif")
    bf_path = os.path.join(path, name + "_bf.tif")

    tifffile.imsave(NADH_path, images[i, 0, :, :])
    tifffile.imsave(FAD_path, images[i, 1, :, :])
    tifffile.imsave(bf_path, images[i, 2, :, :])