sentence = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
words = sentence.split()
single = [1, 5, 6, 7, 8, 9, 15, 16, 19]
elements = []
answer = {}

for i in range(len(words)):
  if i+1 in single:
    elements += words[i][0]
  else:
    elements += words[i][0]
    elements[i] += words[i][1]
  answer[elements[i]] = i+1     #1番目を先頭とする

print(answer)
