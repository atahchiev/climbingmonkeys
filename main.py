p = 9

try:
	1/0
	p = 1
except:
	print(p)
print(p)