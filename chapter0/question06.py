# 参考: https://note.nkmk.me/python-set/#set

def alphabet_ngram(n, text, group): # question05のものを一部改変
  alphabets = text.replace(' ', '').replace(',', '').replace('.', '')
  for i in range(len(alphabets) - n + 1):
    output = ''
    for j in range(n):
      output += alphabets[i + j]
    group.add(output.rstrip())

text_A = 'paraparaparadise'
text_B = 'paragraph'
group_X = set() # {}だと辞書型扱いされるので空の集合型生成にはset()を利用
alphabet_ngram(2, text_A, group_X)
group_Y = set()
alphabet_ngram(2, text_B, group_Y)
print('group_X = ' + str(group_X))
print('group_Y = ' + str(group_Y))
print('-----------------------------------------------')
print('(1) 和集合 X ∨ Y = ' + str(group_X|group_Y))
print('(2) 和集合 X ∧ Y = ' + str(group_X&group_Y))
print('(3) 差集合 X - Y = ' + str(group_X-group_Y))
print('(4) 差集合 Y - X = ' + str(group_Y-group_X))
if 'se' in group_X:
  se_X = True
else:
  se_X = False
if 'se' in group_Y:
  se_Y = True
else:
  se_Y = False
print('(5) Xが"se"を含むか判定 : ' + str(se_X))
print('(6) Yが"se"を含むか判定 : ' + str(se_Y))
