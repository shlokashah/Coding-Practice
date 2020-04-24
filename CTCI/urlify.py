string = input("Enter a string")
l = list(string)
# l.strip()
print(l)
l1=[]
for i in l:
	if i == " ":
		l1.append("%20")
	else:
		l1.append(i)
print(l1)
string = "".join(l1)
print(string)
