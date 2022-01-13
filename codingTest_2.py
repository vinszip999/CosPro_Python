# 모의고사 2회

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
