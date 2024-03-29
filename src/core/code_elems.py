import numpy as np
import math
from itertools import product

def codigo_lineal(MatrizG,z,vectores):
    codigos = []
    if len(vectores[0]) > 1:
        for i in vectores:
            val = np.dot(i, MatrizG)
            codigos.append(val)
        codigos = limpieza_codigo(codigos,z)
    else:
        for i in vectores:
            val = i*MatrizG
            codigos.append(val[0])
        codigos = limpieza_codigo(codigos,z)
    return codigos

def limpieza_codigo(codigos, z):
    for i in codigos:
        h = 0
        for j in i:
            if j >= z:
               t = j % z
               i[h] = t
            h = h + 1
    return codigos

def gen_vector(z, x):
    return list(product(range(z), repeat=x))

def crear_matriz(vectores):
    matriz = np.array(vectores)
    return matriz

def codigo_lineal_print(matriz):
    codigos = []
    for i in matriz:
        codigo = ''
        for j in i:
            codigo = codigo + str(j)
        codigos.append(codigo)
    return codigos

def parametro_k(codigos,z):
    C = len(codigos)
    k = math.log(C,z)
    return int(k)

def elementosos(vector):
    elementos = ''
    for i in vector:
        elementos = elementos + i
        elementos = elementos + ' '
    return elementos

def ejecutable(matG,z):
    vectores = gen_vector(z,len(matG))
    vectores = np.array(vectores)
    codigos = codigo_lineal(matG,z,vectores)
    matrizO = crear_matriz(codigos)
    elem = codigo_lineal_print(matrizO)
    k = parametro_k(elem,z)
    el = elementosos(elem)
    return {"codigos": elem, "n": len(matG), "k": k}