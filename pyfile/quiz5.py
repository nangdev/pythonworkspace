from random import *

con='O'
count = 0

for x in range(1,51):
    time = randint(5,50)

    if time>=5 and time<=15:
        print("[{0}] {1}번째 손님 (소요시간 : {2}분".format(con, x, time))
        count += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분".format(x, time))

print()
print("총 탑승 승객 : {0} 분".format(count))