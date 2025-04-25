file = 'popular-names.txt'
names = set() # 名前の集合

with open(file) as reader:
	texts = reader.readlines()
	for i in range(len(texts)):
		names.add(texts[i].split()[0])
	print(len(names))
