N = 10
flag = 0

with open('popular-names.txt') as f:
  texts = f.readlines()
  for i in range(N):
    print(texts[i])
