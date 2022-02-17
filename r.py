data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了,總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len += len(d)

print('平均是', sum_len / len(data))


new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')


good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言提到good')
print(good[0])

文字計數
w_c = {} #word_count

for d in data:
	words = d.split(' ')
	for word in words:
		if word in w_c:
			w_c[word] += 1
		else:
			w_c[word] = 1
for word in w_c:
	if w_c[word] > 1000000:
		print(word, w_c[word])



while True:
	word = input('請問你想查什麼字: ')
	if word == 'q':
		break
	if word in w_c:		
		print(word, '出現過的次數為: ', w_c[word])
	else:
		print('這個字沒有出現過喔!')
print('感謝使用')

