import math
#n + k^2 = m^2!!
def main():
    num_tiles = int(input())
    k = 1
    if num_tiles == 1:
        print('impossible')
        exit()
    while True:
        m = num_tiles + (k * k)
        if math.sqrt(m).is_integer():
            print(int(math.sqrt(m)), k)
            exit()
        k += 1
        if m < k*k:
            print('impossible')
            exit()

main()