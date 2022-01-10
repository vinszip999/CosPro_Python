# 연산자의 특이 사항
# 증감연산자
a = 1
# a++ 사용안됨!!
a += 1  # a=a+1
print(a)

# 나누기
a, b = 23, 4
c = a/b
print(c, type(c))

d = int(a/b)
print(d, type(d))

e = a//b
print(e, type(e))

# 논리 연산자
a = 5
b = 7
print((a > b) and (a > 0))
print(not(1 < a < 10))

# if문 조건식
var = 10
if var == 10:
    print("2space")
    print("4space")
    print("tab")

# 리스트 선언과 접근
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)
print("number is", type(numbers), len(numbers))

print(numbers[0])
print(numbers[-1])

# 리스트 값 추가 (P28)==> append
li = [1, 2, 3, 4, 5]
li.append(6)
print(li[5])

# 리스트 안에 또 다른 리스트를 한꺼번에 추가
first = [1, 2, 3]
second = [10, 20, 30]
first.append(second)
print(first)
# print(first[4])

first1 = [1, 2, 3]
second1 = [10, 20, 30]
first1 = first1 + second1
print(first1)
print(first1[4])

# 리스트 복사
first2 = [1, 2, 3]
second2 = first2
print(first2, " vs ", second2)

# 리스트 처리 ==> 최대/최소 구하기 ==> 정렬하고 구하기
arr = [1, 2, -4, 56, 8, 89, 77, 23, 4, 22]
arr.sort()
print("정렬 후 : ", arr)
min = arr[0]
max = arr[len(arr)-1]
print("min : ", min, "max : ", max)

# 리스트 처리 ==> 특정요소 찾기
arr2 = [1, 2, 8, 56, 8, 89, 77, 23, 4, 22]
index = arr2.index(8)
print(index)

# 리스트 처리 ==< 갯수
arr3 = [1, 2, 8, 56, 8, 89, 77, 23, 4, 22]
search_value = 8
count = arr3.count(search_value)
if count == 0:
    print("찾을 수 없음")
else:
    print(search_value, "가", count, "개 있음")

# 리스트 처리 ==> 복사 (append) 리스트.copy() 동일
a = [1, 2, 3, 4, 5]
b = []
for i in a:
    b.append(i)
print(a, "vs", b)
a[0] = 10
print(a, "vs", b)

# 리스트 처리 ==> 추출 ==> ":"
s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
sliced = s[:4]
print(sliced)

sliced = s[4:]
print(sliced)

sliced = s[5:7]
print(sliced)

#P44 문자 함수 ==> ord, chr

ch = 'b'
ascii_code = ord(ch)
ascii_char = chr(97)

print(ascii_code , ", " , type(ascii_code))
print(ascii_char)

#p47 count, find, index

string = "python, this is string constant"
print(string)
substring = "is"
print(substring, "01", string.count(substring))
print(substring, "01", string.find(substring))
print(substring, "01", string.index(substring))


# 문제풀이 1) 함수 작성
# 티셔츠 주문 수량 구하는 함수 작성

# 함수 정의
def solution(shirt_size):
    answer = [0, 0, 0, 0, 0, 0]
    # answer = [0 for _ in range(6)]

    for size in shirt_size:
        if size == "XS":
            answer[0] += 1
        elif size == "S":
            answer[1] += 1
        elif size == "M":
            answer[2] += 1
        elif size == "L":
            answer[3] += 1
        elif size == "XL":
            answer[4] += 1
        elif size == "XXL":
            answer[5] += 1

    return answer

# 테스트 매개 변수 주어짐
shirt_size = ["XS", "S", "XXL", "L", "XL", "XXL"]
ret = solution(shirt_size)

# 출력 결과
print("주문 결과 ", ret, "입니다.")

