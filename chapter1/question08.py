# 参考: https://qiita.com/ell/items/6eb48e934a147898d823

# 暗号文の仕様
# 英小文字以外はそのまま出力される
# 英小文字はa⇔z, b⇔y ...と変換

def cipher(text):
  new_text = ''
  for i in range(len(text)):
    if ord(text[i]) >= 97 and ord(text[i]) <= 122:
      new_text += chr(219 - ord(text[i]))
    else:
      new_text += text[i]
  print('文字列 ' + text + ' の変換後文字列 : ' + new_text)

cipher('I am ricky0614.')
print('---------------------------------------')
cipher('自然言語処理は英語でNatural Language Processing')
print('---------------------------------------')
cipher('abcdefghijklmnopqrstuvwxyz')
