import math
number = int(input())
number = (list(str(number)))
s=0
while s!=1:
	for i in number:
		s = s+ math.pow(int(i),2)
	s = 0

if s == 1:
	print("Happy Number")
