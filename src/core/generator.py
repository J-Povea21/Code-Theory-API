from itertools import combinations
from src.utils.helpers import code_exists
import math

def generator_matrix(code: list, z: int) -> dict:

    if not code:
        return {"success" : False,"message": "No code was provided"}

    try:
    
        n = len(code[0])
        if not check_codewords(code, z):
            return {"success" : False,"message": "Invalid code"}
        elif not code_exists(code, n, z):
            return {"success" : False,"message": "The code does not exist"}
        
    
        m = len(code)
        k = math.floor(math.log(m)/math.log(z))

        new_code = remove_module(code)
        base = check_bases(new_code, k, z, n)
        matrix = base_to_matrix(base)

        return {
                "success" : True,
                "matrix": matrix,
                "n": n,
                "k": k
        }    

    except Exception as e:
        return {"success" : False,"message": e.args[0]}     
    

def check_codewords(codewords: list, z: int) -> bool:
    lenght = len(codewords[0])
    for element in codewords:
        if len(element) < lenght or len(element) > lenght:
            return False
        
        for digit in element:
            if int(digit) >= z:
                return False
    return True

def remove_module(codewords: list) -> list:
    pos = 0
    for i in codewords:
        count = 0
        len(i)
        for j in i:
            if int(j) == 0:
                count = count + 1
        pos = pos + 1
        if count == len(i):
            codewords.pop(pos - 1)
    return codewords

def generate_combinations(array: list, value: int):
    return list(combinations(array, value))

def check_bases(array: list, k: int, z: int, lenght: int) -> list|None:
    combinations = generate_combinations(array, k)

    for comb in combinations:
        products = []
        sum_products = []
        found_words = []

        if len(comb) > 1:
               sum_combinations =  get_sums(comb, lenght, z)
               connected_list = list(comb) + sum_combinations
        else:
           connected_list = comb
        if z > 2:
                products = check_products(connected_list, z)
                sum_products = get_sums(products, lenght, z)
        for codeword in array:
            checker = False

            if codeword in connected_list or codeword in products or codeword in sum_products:
                checker = True
            found_words.append(checker)
       
        if all(found_words):
            return comb
        
    return None


def check_products(elements: list, z: int) -> list:
    product_chats = []
    for element in elements:
        for i in range(2,z):
            product = ""
            for d in range(len(element)):
                  product = product + str(int(element[d])*i % z)
            product_chats.append(product)
    return product_chats

def get_sums(comb: list, lenght: int, z: int) -> list:
    sum_combinations = []
    for i in range (2, len(comb)+1):
        groups = generate_combinations(comb,i)
        for group in groups:
            res_word = ""
            for j in range(lenght):
                group_sum = 0
                for element in group:
                    group_sum += int(element[j] )
                group_sum = group_sum % z
                res_word = res_word + str(group_sum)
            sum_combinations.append(res_word)
    return sum_combinations

def base_to_matrix(base: list) -> list[list]:
  rows = len(base)
  cols = len(base[0])
  matrix = [[None] * cols for _ in range(rows)] 
  for i in range(rows):
    for j in range(cols):
      matrix[i][j] = int(base[i][j])
  return matrix