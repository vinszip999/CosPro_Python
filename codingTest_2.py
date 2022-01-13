# 모의고사 2회

# 01 축구장 임대료를 구하는 함수 빈칸 채우기
# 1. n*(n-1)
# 2. n


# 02 축구화 주문 수량을 구하는 함수 완성하기
# def solution(shoes_size):
#     answer = [0 for _ in range(6)]  # answer = [0, 0, 0, 0, 0, 0]
#     for size in shoes_size:  # for x in shoes_size:
#         if size == "7":  # size를 다 x로
#             answer[0] += 1
#         elif size == "7.5":
#             answer[1] += 1
#         elif size == "8":
#             answer[2] += 1
#         elif size == "8.5":
#             answer[3] += 1
#         elif size == "9":
#             answer[4] += 1
#         elif size == "9.5":
#             answer[5] += 1
#
#         return answer


# 03 방문객 수의 차이를 구하는 함수의 빈칸 채우기

# 1. i != num
# 2. func_c(visitor)
# 3. func_c(visitor_removed)
# 4. func_b(max_first, max_second)


# 04 학점별 인원수를 구하는 함수의 빈칸 채우기
# 1. [0 for i in range(5)]
# 2. scores


# 05 빈도(출현 회수)를 구하는 함수의 빈칸 채우기
# 1. i != 0 and ret > 1
# 2. func_a(arr)
# 3. func_b(counter)


# 06 몸무게가 큰 사람의 수를 구하는 함수 수정하기
# if w < k: --> if w > k:  # 부등호 방향 반대로 바뀜


# 07 문자열 내 특정 문자를 바꾸는 함수 수정하기 **
# n = ord(c) - ord('i') --> n = ord('i') - ord(c)


# 08 이름에 특정 문자가 포함된 개수를 구하는 함수 수정하기 p.199
# if char.find('A') or char.find('K'):
# -->
# if char.find('A') > -1 or char.find('K') > -1:  #find는 -1을 반환, -1은 True


# 09 제품 포장을 위한 포장 상자의 개수를 구하는 함수 수정하기
# size += ((i + 1)**2)
# -->
# size += ((i + 1)**2) * (o[i])  # 수량을 곱해야 함


# 10 ISBN 규칙을 확인하는 함수 작성하기
# def sum_isbn(isbn):
#     sum = 0
#     for i in range(len(isbn)):
#         c = int(isbn[i])
#         if i % 2:
#             w = 3
#         else:
#             w = 1
#         sum += w * c
#     return sum
#
#
# def solution(isbn):
#     print(isbn)
#     answer = ''
#     sum = sum_isbn(isbn[:-1])  # isbn[:12]
#     r = 10 - (sum % 10)
#     if r == 10:
#         answer = '0'
#     else:
#         answer = str(r)
#     return answer
