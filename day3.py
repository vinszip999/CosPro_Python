# 문제 16
# 키가 큰 사람의 수를 구하는 함수 수정하기

# def solution(height, k):
#     answer = 0
#     n = len(height)
#
#     # 첫 번째 방법
#     for h in height:
#         if h > k:
#             answer += 1
#     return answer
#
#     # 두 번째 방법
#     # index = 0
#     # while index < n:
#     #     if height[index] > k:
#     #         answer += 1
#     #     index += 1
#     # return answer
#
#
# height = [165, 170, 175, 180, 184]
# k = 175
# ret = solution(height, k)
#
# print("solution 함수의 반환 값은 ", ret, "입니다.")


# 문제 17
# 문자열 내 특정 문자를 바꾸는 함수 수정하기

# def solution(s):
#     s_list = list(s)
#     n = len(s)
#     for i in range(n):
#         if s_list[i] == 'a':
#             s_list[i] = 'z'
#         elif s_list[i] == 'z':
#             s_list[i] = 'a'
#
#     return "".join(s_list)
#
# name = 'james'
# ret = solution(name)
#
# print("solution 함수의 반환 값은 ", ret, "입니다.")


# 문제 18
# 이름에 특정 문자가 포함된 사람의 수를 구하는 함수 수정하기

# def solution(name_list):
#     answer = 0
#     for name in name_list:
#         for n in name:
#             if n == 'j' or n == 'k':
#                 answer += 1
#                 break
#     return answer
#
# names = ['james', 'kim john', 'jokin']
# ret = solution(names)
#
# print("solution 함수의 반환 값은 ", ret, "입니다.")


# 문제 19
# 거스름돈을 계산하는 함수 작성하기

# def solution(price, money):
#     # answer = 0
#     # total = 0
#     # for i in price:
#     #     total += i
#     # answer = money-total
#     # if answer < 0:
#     #     answer = -1
#     # return answer
#
#     # 거스름돈 방법 2> 하나씩 빼기
#     answer = money
#     for i in price:
#         answer -= i
#     if answer < 0:
#         answer = -1
#     return answer
#
# price = [1000, 5000, 500, 2000]
# money = 10000
# ret = solution(price, money)
#
# print("solution 함수의 반환 값은 ", ret, "입니다.")


# 문제 20
# k번째로 작은 수를 찾는 함수 작성하기
def solution(arr, k):
    answer = 0
    temp = []

    # 첫 번째 방법
    for a in arr:
        for b in a:
            temp.append(b)

    # 두 번째 방법
    # for i in range(len(arr)):
    #     for j in range(4):
    #         temp.append(arr[i][j])

    temp.sort()
    answer = temp[k-1]

    return answer

arr = [[5, 12, 4, 31], [24, 13, 11, 2], [43, 44, 19, 26], [33, 65, 20, 21]]
k = 4
ret = solution(arr, k)

print("solution 함수의 반환 값은 ", ret, "입니다.")
