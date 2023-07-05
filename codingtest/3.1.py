n = 1800
count = 0 

coin_types = [500,100,50,10]
for i in coin_types:
    count += n // i
    n %= i

print(count)