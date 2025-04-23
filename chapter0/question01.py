text_A = 'パタトクカシーー'
answer = ''

for i in range(int(len(text_A)/2)):
  answer += text_A[2*i+1]

print(text_A)
print(answer)
