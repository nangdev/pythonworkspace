from random import randint


def quick_sort(arr):
    # 리스트가 하나 이하의 원소를 가지면 종료
    if len(arr) <= 1: return arr
    
    pivot, tail = arr[0], arr[1:]
    
    lside = [x for x in tail if x <= pivot]
    rside = [x for x in tail if x > pivot]
    
    return quick_sort(lside) + [pivot] + quick_sort(rside)

num = int(input("몇개의 정수? "))
li = []
for i in range(num):
    li.append(randint(-9,9))
print(li)
result = quick_sort(li) 
print(result)