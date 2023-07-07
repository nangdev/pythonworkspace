def weight(h,g):
    if g == "남성":
        return h * h * 22
    else:
        return h * h * 21


gender = input("성별을 입력하세요:")
height = int(input("키를 입력하세요:"))
stdw = round(weight(height / 100,gender),2)

print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height,gender,stdw))

