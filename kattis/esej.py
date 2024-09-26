import itertools
import random

def generate_unique_strings(n):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    unique_strings = []
    
    # Generate strings of length 1 to 15
    for length in range(1, 16):
        for chars in itertools.product(alphabet, repeat=length):
            unique_strings.append(''.join(chars))
            if len(unique_strings) >= n:
                return random.sample(unique_strings, n)  # Return a random sample of size n

    return random.sample(unique_strings, n)

# Example usage
a,b = map(int, input().split())
num_strings = max(a, b//2)
unique_strings = generate_unique_strings(num_strings)
print(" ".join(unique_strings))
