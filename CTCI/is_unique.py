string_1 = input("Enter the string")
lis = list(string_1)
d = {}
for i in lis:
	if d.get(i):
		d[i] = d[i]+1
	else:
		d[i] = 1
flag = 0
for i,v in d.items():
	if v == 2:
		flag = 1
		break
if flag == 0:
	print("Unique")
else:
	print("Not unique")
print(d)
print(lis)