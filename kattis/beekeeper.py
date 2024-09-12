vowels = "aeiouyAEIOUY"
while True:
    n = int(input())
    if n == 0:
        break
    words = [input() for _ in range(n)]
    max = -1
    m_word = ""
    for i in words:
        double = 0
        total_doubles = 0
        vowel = None
        for j in i:
            if j in vowels and vowel == None:
                double = .5
                vowel = j
            elif j in vowels and j == vowel:
                vowel = None
                double = 0
                total_doubles += 1
            elif j in vowels:
                double = .5
                vowel = j
            else:
                double = 0
                vowel = None
        
        if max < total_doubles:
            m_word = i 
            max = total_doubles
    
    print(m_word)