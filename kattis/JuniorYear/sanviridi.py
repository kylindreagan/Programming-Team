import bisect

n = int(input())

guess_to_name, ideas = {}, []

for i in range(n):
    name, guess = map(str, input().split())
    guess = int(guess)
    guess_to_name[guess] = name


sorted_guesses = sorted(guess_to_name.keys())
for _ in range(int(input())):
    query = int(input())
    
    # Find the largest guess <= query using binary search
    idx = bisect.bisect_right(sorted_guesses, query) - 1
    
    if idx == -1:
        print(":(")
    else:
        best_guess = sorted_guesses[idx]
        print(guess_to_name[best_guess])