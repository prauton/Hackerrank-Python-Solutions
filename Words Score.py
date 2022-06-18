def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    score = 0
    
    for n in words:
        z = 0
        count = 0
        for i in n:
            if is_vowel(i):
                z += 1
            else:
                pass
        if z % 2 == 0:
            count += 2
        else:
            count += 1
        score += count
    return score


n = int(input())
words = input().split()
print(score_words(words))
