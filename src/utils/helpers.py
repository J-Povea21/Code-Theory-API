from math import comb

def min_distance(code: list) -> int:
    
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
    m = len(code)
    d = min_distance(code)
    t = (d-1)//2

    # Singleton bound
    singleton = z**(n-d+1)

    # Hamming bound
    hamming = (z**n)/(sum( [ comb(n,j)*(z-1)**j for j in range(t+1) ] ) )

    return singleton <= m <= hamming