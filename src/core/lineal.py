import numpy as np
import math
from itertools import product
from src.utils.helpers import arr_to_str

def get_lineal_code(matrix,z,arrays):
    codewords = []
    if len(arrays[0]) > 1:
        for i in arrays:
            val = np.dot(i, matrix)
            codewords.append(val)
        codewords = clean_codes(codewords,z)
        print(codewords)
    else:
        for i in arrays:
            val = i*matrix
            codewords.append(val[0])
        codewords = clean_codes(codewords,z)
    return codewords

def clean_codes(codewords, z):
    for i in codewords:
        h = 0
        for j in i:
            if j >= z:
               t = j % z
               i[h] = t
            h = h + 1
    return codewords

def generate_vector(z, x) -> np.array:
    return np.array( list( product(range(z), repeat=x) ) ).tolist()

def create_matrix(arrays):
    matrix = np.array(arrays)
    return matrix

def get_k(codewords,z):
    C = len(codewords)
    k = math.log(C,z)
    return int(k)

def lineal_code(gen_matrix,z):
    try:
        arrays = generate_vector(z,len(gen_matrix))
        arrays = np.array(arrays)
        codewords = get_lineal_code(gen_matrix,z,arrays)
        matrixO = create_matrix(codewords)
        elem = arr_to_str(matrixO)
        return {
            "success": True,
            "codewords": arr_to_str(matrixO),
            "n": len(gen_matrix[0]), 
            "k": get_k(elem,z)
            }
    except Exception as e:
        return {"success": False, "message": e.args[0]}