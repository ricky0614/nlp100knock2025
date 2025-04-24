# 参考: https://mojitoba.com/2019/09/23/what-is-ngram/

def word_ngram(n, text): # 入力は文字列を想定
  words = text.split()
  elim_words = []
  for i in range(len(words)):
    elim_words.append(words[i].replace(',', '').replace('.', ''))
  for i in range(len(words) - n + 1):
    output = ''
    for j in range(n):
      output += elim_words[i + j] + ' '
    print(output.rstrip())

def alphabet_ngram(n, text): # 入力は文字列を想定
  alphabets = text.replace(' ', '').replace(',', '').replace('.', '')
  for i in range(len(alphabets) - n + 1):
    output = ''
    for j in range(n):
      output += alphabets[i + j]
    print(output.rstrip())


text = "I am an NLPer"

print('文字tri-gram:')
alphabet_ngram(3, text)
print('---------------------------------')
print('単語bi-gram:')
word_ngram(2, text)
