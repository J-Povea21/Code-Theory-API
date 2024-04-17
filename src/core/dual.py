from src.utils.helpers import *
from .generator import generator_matrix
from .lineal import generate_vector, lineal_code

def dual(code: list[str] | list[list[int]] , z: int = 2) -> list:
    try:
    
        # In case we get the code elements, we create the generator matrix
        # Otherwise we just transpose the given matrix

        if type(code[0]) == str:
            codewords = code[:]
            G = generator_matrix(code, z)["matrix"]
        else:
            G = code
            codewords = lineal_code(G, z)["codewords"] 
    
        G = transpose(G)
        array = generate_vector(z, len(G)) # It generates the vectors in the field z

        dual_code = arr_to_str( [element for element in array if matrixial_zero(element, G, z)] )
        dual_type = code_type(codewords, dual_code, z)

        return {"success": True, "url": code_to_txt(dual_code, dual_type)}
    except Exception as e:
        return error_response(e.args[0])


def code_type(lineal_code: list[str], dual_code: list[str], z: int = 2) -> str:
    try:
       if is_self_dual(lineal_code, dual_code, z):
           return "Self-Dual"
       elif is_self_orthogonal(lineal_code, dual_code, z):
            return "Self-Orthogonal"
       
       return "Linear code" 
        
    except Exception as e:
        return error_response(e.args[0])
    
def is_self_dual(lineal_code: list[str], dual_code: list[str],  z: int = 2) -> bool:
    try:
        return compare_lists(lineal_code, dual_code)
    except Exception as e:
        return error_response(e.args[0])

def is_self_orthogonal(lineal_code: list, dual_code: list[str],  z: int = 2) -> bool:
    try:
        
        for codeword in dual_code: # Here we check if the code it's a subset of the linear code
            if codeword in lineal_code:
                return True
    
        return False   
    except Exception as e:
        return error_response(e.args[0])

