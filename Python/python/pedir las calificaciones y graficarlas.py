# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 09:11:44 2022

@author: jhazy
"""

import numpy as np
import matplotlib.pyplot as plt

def GetNameStudent(numStudent = 5):
    student = [] 
    for i in range(0, numStudent):
        student.append( input('Nombre del alumno: ') )
    return student

def GetSchoolGrades(numGrades = 5):
    grades = []
    for i in range(0, numGrades):
        grades.append( int(input('Calificación a asignar: ')) )
    return grades

    

def GraphResult():
    fig, ax=plt.subplots()
    ax.set_ylabel('Valores')
    ax.set_title('Calificaciones')
    plt.barh(GetNameStudent(),GetSchoolGrades(), alpha=0.8, color='blue')
    plt.show()


GraphResult()
    

    