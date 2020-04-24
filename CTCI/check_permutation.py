string_1 = input()
string_2 = input()
if len(string_1) != len(string_2):
	print("Not permutable")
else:
	l1 = list(string_1)
	l2 = list(string_2)
	l1 = l1.sort()
	l2 = l2.sort()
	if l1 == l2:
		print("permutable")
	else:
		print("Not permutable")
