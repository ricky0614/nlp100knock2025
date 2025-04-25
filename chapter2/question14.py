N = 10
flag = 0

with open('popular-names.txt') as f:
  texts = f.readlines()
  lines = []
  for i in range(N):
    lines.append(texts[i].split()[0])
    print(lines[i])
