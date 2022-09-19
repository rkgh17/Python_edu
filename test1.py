# 연산자
# 산술 : +, -, *, /, **, %, //, =, +=, -=, /=, %=, //= (++, --는 없음)
#        + : 양쪽이 문자열이면 연결
# 비교 : ==, !=, >=, <=, <, >, is None, is Not None
# 논리 : and, or, not
# NULL이없고 None 
# 파이썬의 키워드(keyword)는 소문자로만 쓴다.
# 상수:None, True, False는 대문자로만

# print() : format(), %
i=3.14
name='황지훈'
print(i)
print(name)

a=None
if a!=None:print(10)
else:print(-10)

a
print(a)
# print('사과값은'+a'원입니다') 
type(a)
print('사과값은'+str(a)+'원입니다')
str(a)
print('사과값은 {}원 입니다.',format(a))
