n = input()
firstH = n.find('h')
lastH = n.rfind('h')
m = n[firstH:lastH]
print(n.replace(m, m[::-1]))