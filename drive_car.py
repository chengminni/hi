dirving = input('請問你有沒有開過車?')
if dirving != '有' and dirving != '沒有':
	print('只能輸入 有/沒有')
	raise SystemExit

age = input('請問你的年齡?')
age = int(age)
if dirving == '有':
	if age >= 18:
		print('你有駕照,你通過測驗了')
	else:
		print('奇怪你怎麼開過車')
elif dirving == '沒有':
	if age >= 18:
		print('你可以考駕照了阿,怎不去考呢!')
	else:
		print('很好再過幾年就可以考駕照了')