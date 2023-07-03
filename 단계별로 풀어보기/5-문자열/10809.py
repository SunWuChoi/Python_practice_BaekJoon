word = input()
alphabet = [-1]*26

for i in range(len(word)):
    num = ord(word[i]) - 97
    if alphabet[num] == -1:
        alphabet[num] = i
print(*alphabet)