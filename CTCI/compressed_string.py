string = input("Enter the input string")
l = list(string)
d = {}
for i in l:
	if d.get(i):
		d[i] = d[i]+1
	else:
		d[i] = 1
print(d)
new_l = []
for i,v in d.items():
	new_l.append(i)
	new_l.append(str(v))
print(new_l)
string_1 = "".join(new_l)
if len(string_1)>len(string):
	print(string)
else:
	print(string_1)

