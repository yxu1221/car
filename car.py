driving = input('請問你有沒有開過車?')
if driving != '有' and driving != '沒有':
		print('只能輸入  有/沒有')
		raise SystemExit
age = input('請問你的年齡是?')
age = int(age)
if driving == '有':
	if age >= 18:
		print('你通過測試囉')
	else:
		print('你怎麼開過車?')
elif driving =='沒有':
	if age >= 18:
		print('你可以考駕照囉，怎麼不考')
	else:
		print('很好在幾年就能考駕照拉~')
else:
	print('只能輸入 有/沒有')

