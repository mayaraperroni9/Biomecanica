import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import c3d
import math
import os
import sys
import glob
import re

#Função para calcular a rotação entre dois planos
def calc_rotation(p1, p2):
    #Calcula o vetor normal ao plano 1
    n1 = np.cross(p1[0], p1[1])
    #Calcula o vetor normal ao plano 2
    n2 = np.cross(p2[0], p2[1])
    #Calcula o vetor normal ao plano 1
    n1 = n1 / np.linalg.norm(n1)
    #Calcula o vetor normal ao plano 2
    n2 = n2 / np.linalg.norm(n2)
    #Calcula o vetor normal ao plano 1
    n1 = n1 / np.linalg.norm(n1)
    #Calcula
    v = np.cross(n1, n2)
    #Calcula
    c = np.dot(n1, n2)
    #Calcula
    s = np.linalg.norm(v)
    #Calcula
    k = np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])
    #Calcula
    R = np.eye(3) + k + np.dot(k, k) * ((1 - c) / (s ** 2))
    return R

#Função para calcular a rotação entre dois planos
def calc_rotation_angle(p1, p2):
    #Calcula o vetor normal ao plano 1
    n1 = np.cross(p1[0], p1[1])
    #Calcula o vetor normal ao plano 2
    n2 = np.cross(p2[0], p2[1])
    #Calcul
    n1 = n1 / np.linalg.norm(n1)
    #Calcula
    n2 = n2 / np.linalg.norm(n2)
    #Calcula
    v = np.cross(n1, n2)
    #Calcula
    c = np.dot(n1, n2)
    #Calcula
    s = np.linalg.norm(v)
    #Calcula
    k = np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])
    #Calcula
    R = np.eye(3) + k + np.dot(k, k) * ((1 - c) / (s ** 2))
    #Calcula
    angle = math.atan2(s, c)
    return angle


    
     
In [ ]:

#função para recebeber os dados e os calcular
def calc_data(data):
    #Calcula a rotação entre os planos
    R = calc_rotation(data[0], data[1])
    #Calcula a rotação entre os planos
    angle = calc_rotation_angle(data[0], data[1])
    #Calcula a rotação entre os planos
    angle = math.degrees(angle)
    #Calcula a rotação entre os planos
    angle = round(angle, 2)
    #Calcula a rotação entre os planos
    return R, angle
     
In [ ]:

#função para plotar os dados de rotação
def plot_data(data, angle):
    #Calcula a rotação entre os planos
    R, angle = calc_data(data)
    #Calcula a rotação entre os planos
    print(R)
    #Calcula a rotação entre os planos
    print(angle)
    #Calcula a rotação entre os planos
    plt.figure()
    #Calcula a rotação entre os planos
    plt.plot(data[0][0], data[0][1], 'r')
    #Calcula a rotação entre os planos
    plt.plot(data[1][0], data[1][1], 'b')
    #Calcula a rotação entre os planos
    plt.show()

     
In [ ]:

def vizualiza(x,y,z, planox, planoy, planoz):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, c='r', marker='o')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim(planox)
    ax.set_ylim(planoy)
    ax.set_zlim(planoz)
    plt.show()

vizualiza(x,y,z, (-10,10), (-10,10), (-10,10))

#Crie uma função em python para a visualização de planos cruzados 3D.

def vizualiza(x,y,z, planox, planoy, planoz):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, c='r', marker='o')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim(planox)
    ax.set_ylim(planoy)
    ax.set_zlim(planoz)
    plt.show()

vizualiza(x,y,z, (-10,10), (-10,10), (-10,10))
