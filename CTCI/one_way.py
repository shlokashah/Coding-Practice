string_1 = input()
string_2 = input()
l = list(string_1)
l1 = list(string_2)
len_1 = len(l)
len_2 = len(l1)
count=0
i=0
j=0
if abs(len_1-len_2)>1:
	print("False")
else:
	while i<len_1 and j<len_2:
		if l[i]!=l1[j]:
			if count==1:
				print("False")
				break
			if len_1>len_2:
				i = i+1
			elif len_1<len_2:
				j = j+1
			else:
				i = i+1
				j = j+1
			count = count +1
		else:
			i = i+1
			j = j+1
	if i < len_1 or j < len_2: 
		count+=1
	if count == 1:
		print("True")
	else:
		print("False")

