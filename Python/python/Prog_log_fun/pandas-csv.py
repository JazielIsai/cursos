# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 08:32:55 2022

@author: jhazy
"""
import pandas as pd

datoestacion = pd.read_csv(r"C:/Users/jhazy/Documents/cursos/Python/python/Prog_log_fun/Aemet2022-01-01.csv", index_col=(0), encoding='latin-1')
print (datoestacion)