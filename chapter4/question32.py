text = '''
メロスは激怒した。
必ず、かの邪智暴虐の王を除かなければならぬと決意した。
メロスには政治がわからぬ。
メロスは、村の牧人である。
笛を吹き、羊と遊んで暮して来た。
けれども邪悪に対しては、人一倍に敏感であった。
'''

import MeCab
tagger = MeCab.Tagger()
print(tagger.parse(text))
result = tagger.parse(text).split()
length = int((len(result) - 1) / 2)  # EOSの分かならず-1
answer = []

for i in range(length - 2):
  if (result[2 * i + 1].startswith('名詞') and
      result[2 * i + 2] == 'の' and
      result[2 * i + 3].startswith('助詞') and
      result[2 * i + 5].startswith('名詞')):
    dummy = result[2 * i] + result[2 * i + 2] + result[2 * i + 4]
    answer.append(dummy)

print(answer)
