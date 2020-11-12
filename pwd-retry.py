password = 'abcd1234'
i = 3  #剩余机会
while True:
	pwd = input('Password: ')
	if pwd == password:
		print('Password Correct!')
		break  #逃出回圈
	else:
		i = i - 1
		print('Wrong Password! ', i, 'Attemp Left')
		if i == 0:
			break