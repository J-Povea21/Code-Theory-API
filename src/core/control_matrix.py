from typing import List
import numpy as np

# Gets the base of the code
def code_base(code):
    base = [] 
    matrix = np.array(code)
    
    for i in range(matrix.shape[1]): 
        for j in range(i, matrix.shape[0]):
            if matrix[j][i] != 0:  
                base.append(matrix[j])
                
                if matrix[j][i] != 0:
                    with np.errstate(divide='ignore', invalid='ignore'):
                        matrix[[i, j]] = matrix[[j, i]]  
                        matrix[j] = matrix[j] // matrix[j][i]
                for k in range(matrix.shape[0]): 
                    if k != j:
                        matrix[k] = matrix[k] - matrix[j] * matrix[k][i]
                break  
    return base 

def get_control_matrix(n: int, k: int, base, z):
    H = [] 
    base_set = set(map(tuple, base))

    while len(H) < n - k:
        row = np.random.choice(z, n)
        if tuple(row) not in base_set:
            H.append(row)
            base_set.add(tuple(row))

    return np.array(H)

def check_matrix(H, code, z):
    
    for codeword in code:
        if np.any(np.dot(H, np.array(codeword).reshape(-1, 1)) % len(z) != 0):
            return False 
    return True 

def control_matrix(n, k, code, z):
    
    base = code_base(code)
    z_set = [i for i in range(z)]
    H = get_control_matrix(n, k, base, z_set)

    while not check_matrix(H, code, z_set):
        H = get_control_matrix(n, k, base, z_set)
    
    return H.tolist()
