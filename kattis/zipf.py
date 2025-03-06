import re

try:
    while True:
        words = {}
        n = int(input())
        total = []
        while True:
            line = input()
            if line == "EndOfText":
                break
            else:
                cleaned_line = re.sub(r'[^a-zA-Z\s]', ' ', line)
                for w in cleaned_line.lower().split():
                    if w not in words:
                        words[w] = 0
                    words[w] += 1

        nth_words = [x for x in words.keys() if words[x] == n]
        
        if nth_words == []:
            print("There is no such word.")
        
        else:
            nth_words.sort()
            for answer in nth_words:
                print(answer)
        
        print()

except EOFError:
    quit()