# 문제 16
# 키가 큰 사람의 수를 구하는 함수 수정하기

def solution(height, k):
    answer = 0
    n = len(height)

    # 첫 번째 방법
    for h in height:
        if h > k:
            answer += 1
    return answer

    # 두 번째 방법
    # index = 0
    # while index < n:
    #     if height[index] > k:
    #         answer += 1
    #     index += 1
    # return answer


height = [165, 170, 175, 180, 184]
k = 175
ret = solution(height, k)

print("solution 함수의 반환 값은 ", ret, "입니다.")


# 문제 17
# 문자열 내 특정 문자를 바꾸는 함수 수정하기

def solution(s):
    s_list = list(s)
    n = len(s)
    for i in range(n):
        if s_list[i] == 'a':
            s_list[i] = 'z'
        elif s_list[i] == 'z':
            s_list[i] = 'a'

    return "".join(s_list)

name = 'james'
ret = solution(name)

print("solution 함수의 반환 값은 ", ret, "입니다.")