x = input()
n = input()

data = list(str(x))
ans =""

for i in data:
    i = (int(i) +n)%10
    ans += str(i)

print ans
