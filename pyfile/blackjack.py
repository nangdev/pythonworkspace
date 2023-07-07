class A:
    def __init__(self, name):
        self.name = name
        print('A')

    def __call__(self):

        print("%s 객체 두두등장" % (self.name))
        self.string = input("어떤 계산을 실행하겠습니까")
        if self.string == '+':
            print("더하기 연산 실행")
        elif self.string == '-':
            print("빼기 연산 실행")
        elif self.string == '*':
            print("곱하기 연산 실행")
        else:
            print("그런 연산은 없습니다")


cal = A("calcul")
cal()
