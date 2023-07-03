word = input()
croatia_word_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for croatia_word in croatia_word_list :
    word = word.replace(croatia_word, '_')
print(len(word))