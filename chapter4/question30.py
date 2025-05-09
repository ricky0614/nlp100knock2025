# 参考: https://qiita.com/automation2025/items/7474deca81fd8f6cda07

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
verb = []

for i in range(length):
  if result[2 * i + 1].startswith('動詞'):
    verb.append(result[2 * i])

print(verb)
