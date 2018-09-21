n = input()
for x in range(0, len(n), 3):
	n = n.replace(n[x], '')

print(n)