# 문제 2

def solution(price, grade):
    answer = 0
    if grade == "S":
        answer = int(price * 0.95)
    if grade == "G":
        answer = int(price * 0.9)
    if grade == "V":
        answer = int(price * 0.85)
    return answer

# 테스트 코드
price1 = 1000
grade1 = "V"
ret1 = solution(price1, grade1)

print("solution 함수의 반환 값은 ", ret1, "입니다.")


price2 = 10000
grade2 = "S"
ret2 = solution(price2, grade2)

print("solution 함수의 반환 값은 ", ret2, "입니다.")


