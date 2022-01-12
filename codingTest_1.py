# 모의고사 1회

# 01 거스름돈을 계산하는 함수 작성하기
# def solution(price, money):
#     answer = 0
#     for i in price:
#         money -= i
#     answer = money
#     if answer < 0:
#         answer = -1
#     return answer


# 02 점수의 총합에서 최고 점수와 최저 점수를  뺄셈하는 함수의 빈칸 채우기
# 1. s.sort()  # s[len(s)-1], s[0] = max(s), min(s) 접근 가능
# 2. b(scores)
# 3. a(scores)


# 03 학습 대상자 수를 구하는 함수 수정하기
# for s in range(len(scores))  # s는 scores 리스트의 요소번호


# 04 관세를 매긴 금액을 구하는 함수 작성하기

# def solution(price, grade):
#     answer = 0
#     if grade == "S":
#         answer = int(price*1.05)  # answer = int(price*(5/100))
#     if grade == "G":
#         answer = int(price*1.10)  # answer = int(price*(10/100))
#     if grade == "V":
#         answer = int(price*1.15)  # answer = int(price*(15/100))
#
#     # return int(answer)  # return 안써도 됨


# 05 정수에 3, 6, 9가 포함되어 있는지 확인하는 함수의 빈칸 채우기
# 1. range(1, number+1)
# 2. current % 10
# 3. current //= 10


# 06 교차점의 개수를 구하는 함수 빈칸 채우기 **
# 1. range(i)
# 2. left_rings[k]


# 07 파일 업로드를 위한 파일 정보를 확인하는 함수의 빈칸 채우기
# 1. file_info
# 2. splited[0] == 'jpeg' and int(splited[2]) < 1000
# split 잘 기억해두기!


# 08 거꾸로 읽어도 같은 회문을 확인하는 함수 수정하기
# before = ''.join(filtered)


# 09 중복되는 문자를 제거하는 함수 수정하기
# characters[i]


# 10 특정 값보다 작은 값을 차는 함수 수정하기
# if i <= average --> if i < average  # 미만이기 때문에!
