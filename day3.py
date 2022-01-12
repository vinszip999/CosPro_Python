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

