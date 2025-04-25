# 参考: https://www.headboost.jp/python-how-to-sort-dict/
# 参考: https://www.headboost.jp/python-lambda/

file = 'popular-names.txt'
names = {} # 名前から登場回数のディクショナリ
names_sort = {} # 登場回数でソート済みのもの

with open(file) as reader:
	texts = reader.readlines()
	for i in range(len(texts)):
		if texts[i].split()[0] in names:
			names[texts[i].split()[0]] += 1
		else:
			names[texts[i].split()[0]] = 1
	# ラムダ式によって辞書の[1]番目の要素(値)でソート
	# reverse = Trueなので降順
	names_sort = sorted(names.items(), reverse = True, key = lambda x:x[1])
	for i in range(len(names_sort)):
		print(names_sort[i])
