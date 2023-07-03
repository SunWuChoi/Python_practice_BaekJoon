word = input()

i, j = 0, len(word)-1

while True:
    if i == j or i > j:
        print(1)
        break
    elif word[i] != word[j]:
        print(0)
        break
    else:
        i += 1
        j -= 1