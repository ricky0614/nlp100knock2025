sentence = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
words = sentence.split()
alphabets = []
answer = []

for i in range(len(words)):
  alphabets.append(words[i].replace(',', '').replace('.', ''))
  answer.append(len(alphabets[i]))
print(answer)
