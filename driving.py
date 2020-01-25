courtry = input('請問你是哪國人: ')
age = int(input('你的年齡: '))
if courtry == '台灣':
	if age >= 18:
		print('你可以考駕照')
	else:
		print('你還不能考駕照')
elif courtry == '美國':
	if age >= 16:
		print('你可以考駕照')
	else:
		print('你還不能考駕照')
