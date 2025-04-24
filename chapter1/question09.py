# 参考: https://pawalog.com/python/ramdom-shuffle

import random

def shuffle_text(text):
  words = []
  words = text.split()
  shuffle_words = []
  shuffle_list = []
  answer = ''
  for i in range(len(words)):
    if len(words[i]) < 5:
      shuffle_words.append(words[i])
    else:
      first = words[i][0]
      last = words[i][len(words[i]) - 1]
      for j in range(len(words[i]) - 2):
        shuffle_list.append(words[i][j+1])
      random.shuffle(shuffle_list)
      shuffle_words.append(first + ''.join(shuffle_list) + last)
      shuffle_list = []
  for i in range(len(shuffle_words)):
    answer += shuffle_words[i] + ' '
  print(answer)

text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
shuffle_text(text)
