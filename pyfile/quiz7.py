def func(a, b) :
  "이것은 함수의 도움말입니다" #몸체 첫 문자열은 함수의 도움말로 정의됨
  b, a = a, b
  return a, b

print(func)
print(type( func))
print(func.__doc__)         # __doc__ 은 함수에 정의된 도움말

print(func(10,20))
c, d = func(1, 2)
print(c, d)



#첫번쨰 프린트 func함수의 주소값 출력
#두번째 프린트 func의 타입인 함수 function을 출력
#세번째 프린트 func의 도움말 부분인 문자열을 출력
#네번쩨 프린트 함수의 내용인 두 매개변수의 값을 바꿔주는 연산 실행
#다섯번째 프린트 함수연산 실행 후 바로 반환값을 c ,d 의값으로 할당한 결과