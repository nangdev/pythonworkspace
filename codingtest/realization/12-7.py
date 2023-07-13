n = input()
inn = []
for i in n:
    inn.append(int(i))
if sum(inn[:len(n)//2]) == sum(inn[len(n)//2:]):
    print("LUCKY")
else:
    print("READY")
