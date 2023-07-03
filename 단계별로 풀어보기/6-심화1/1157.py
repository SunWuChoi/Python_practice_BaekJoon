word = input()
alphabet = [0]*26
for char in word:
    char_num = ord(char.upper())-65
    alphabet[char_num] += 1
max_value = max(alphabet)
max_count = 0

for count in alphabet:
    if count == max_value:
        max_count += 1
if max_count > 1:
    print("?")
else:
    print(chr(alphabet.index(max_value)+65))