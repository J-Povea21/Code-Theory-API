from math import comb
import numpy as np

def min_distance(code: list) -> int:
    
    if len(code) == 1:
        return 0

    def count_diff(a: str, b: str) -> int:
        count = sum(1 for char1, char2 in zip(a, b) if char1 != char2)
        return count
    
    min_dist = float('inf')
    for i in range(len(code)):
        for j in range(i+1, len(code)):
            # Count the number of different digits between the current elements
            count = count_diff(code[i], code[j])
            
            if count < min_dist:
                min_dist = count
    
    return min_dist


def code_exists(code: list, n: int, z: int) -> bool:
    try:
        m = len(code)
        d = min_distance(code)
        t = (d-1)//2

        # Singleton bound
        singleton = z**(n-d+1)

        # Hamming bound
        hamming = (z**n)/(sum( [ comb(n,j)*(z-1)**j for j in range(t+1) ] ) )

        return singleton <= m <= hamming

    except Exception as e:
        return False

def matrix_multp(a: list, b: list, z: int = 2) -> list:
    return [ [ ( sum(x*y for x,y in zip(a_row,b_col) ) % z) for b_col in zip(*b) ] for a_row in a ]

def matrixial_zero(vector: list, matrix: list, z: int = 2) -> list:
    multp = [ ( sum(x*y for x,y in zip(vector,b_col) ) % z) for b_col in zip(*matrix) ]
    return sum(multp) == 0

def transpose(matrix: list) -> list:
    return np.array(matrix).transpose().tolist()

def arr_to_str(array: list[list[int]]) -> list:
    return [''.join([str(j) for j in i]) for i in array]

def compare_lists(a: list, b: list) -> bool:

    if len(a) != len(b):
        return False

    return all( [True if x in b else False for x in a] )

def code_to_txt(code: list[str], type: str, filename: str = "files/code.txt") -> None:
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        f.write(f"Code: {code}\n")
        f.write(f"Type: {type}")
    return filename


def response(data: dict) -> dict:
    return {"success": True, **data}

def error_response(msg: str) -> dict:
    return {"success": False, "message": msg}