file = 'popular-names.txt'
N = 10
file_name = 'file_'
extension = '.txt'

with open(file) as reader:
	texts = reader.readlines()
	numｂer = int(len(texts) / N)
	for i in range(N):
		data_onefile = []
		with open(file_name + str(i + 1) + extension, mode = 'w') as writer:
			for j in range(number):
				writer.write(str(texts[number * i + j]))
