import math

def find_solution(num_tiles):
    #Find m,k such that num_tiles = m² - k²
    for a in range(1, int(math.isqrt(num_tiles)) + 1):
        if num_tiles % a == 0:
            b = num_tiles // a
            if (a + b) % 2 == 0 and (b - a) % 2 == 0:
                m = (a + b) // 2
                k = (b - a) // 2
                if k >= 0: 
                    return m, k
    
    return None

def main():
    num_tiles = int(input())
    result = find_solution(num_tiles)
    
    if result:
        print(result[0], result[1])
    else:
        print('impossible')

if __name__ == "__main__":
    main()