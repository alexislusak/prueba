# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 17:05:58 2018

@author: admin
"""

from matplotlib import pyplot as plt
import numpy as np

FRET = np.loadtxt('FRET0.5M0.0050s3.csv', delimiter=',')
FRET5 = np.loadtxt('FRET5uM1s3.csv', delimiter=',')
FRET50 = np.loadtxt('FRET50uM0.18s3.csv', delimiter=',')
R6G = np.loadtxt('R6GFlu0.5M0.0050s3.csv', delimiter=',')
Flu = np.loadtxt('Flu0.5M0.0050s3.csv', delimiter=',')
R6G50 = np.loadtxt('R6G50uM0.18s3.csv', delimiter=',')
Flu50 = np.loadtxt('Flu50uM0.18s3.csv', delimiter=',')
R6G5 = np.loadtxt('R6G5uM1s3.csv', delimiter=',')
Flu5 = np.loadtxt('Flu5uM1s3.csv', delimiter=',')

aFRET = np.loadtxt('AbsFRETFlu0.5M0.0050s3.csv', delimiter=',')
aFRET5 = np.loadtxt('AbsFRET5uM0.005s3.csv', delimiter=',')
aFRET50 = np.loadtxt('AbsFRET50uM0.005s3.csv', delimiter=',')
aR6G = np.loadtxt('AbsR6GFlu0.5M0.0050s3.csv', delimiter=',')
aFlu = np.loadtxt('AbsFluFlu0.5M0.0050s3.csv', delimiter=',')
aR6G50 = np.loadtxt('AbsR6G50uM0.005s3.csv', delimiter=',')
aFlu50 = np.loadtxt('AbsFlu50uM0.005s3.csv', delimiter=',')
aR6G5 = np.loadtxt('AbsR6G5uM0.005s3.csv', delimiter=',')
aFlu5 = np.loadtxt('AbsFlu5uM0.005s3.csv', delimiter=',')

f=np.loadtxt('Fondo0.5M0.0050sprom(ldo,int,err).csv', delimiter=',')
fondo=np.zeros((3648,3), dtype=float)
fondo[:,0]=f[0:3648]
fondo[:,1]=f[3648:7296]
yerrfondo=np.std(fondo[0:500,1])
for i in range(len(fondo[:,1])):
    if fondo[i,1] <= yerrfondo:
        fondo[i,1]=yerrfondo

#dia 3


aFRET50b = np.loadtxt('BufFRET50uM0.005s3.csv', delimiter=',')
aFlu50b = np.loadtxt('BufFlu50uM0.005s3.csv', delimiter=',')
aR6G50b = np.loadtxt('BufR6G50uM0.005s3.csv', delimiter=',')
aR6G50 = np.loadtxt('AbsR6G50uM0.005s3.csv', delimiter=',')
aFlu50 = np.loadtxt('AbsFlu50uM0.005s3.csv', delimiter=',')
aFRET50 = np.loadtxt('AbsFRET50uM0.005s3.csv', delimiter=',')


f=np.loadtxt('Fondo0.5M0.0050sprom(ldo,int,err).csv', delimiter=',')
fondo=np.zeros((3648,3), dtype=float)
fondo[:,0]=f[0:3648]
fondo[:,1]=f[3648:7296]
yerrfondo=np.std(fondo[0:500,1])
for i in range(len(fondo[:,1])):
    if fondo[i,1] <= yerrfondo:
        fondo[i,1]=yerrfondo

