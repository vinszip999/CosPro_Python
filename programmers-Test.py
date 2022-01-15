# 프로그래머스 Cospro Python 2급 모의고사

# 거스름돈
# 방법1
def solution(price1, money1):
    sum = 0
    answer = 0
    for i in price1:
        sum += i

        # if len(price) == 0:
        #     return sum

    answer = money1 - sum

    if sum > money1:
        return -1
    else:
        return answer

price1 = [2100, 3200, 2100, 800]
money1 = 10000
ret1 = solution(price1, money1)  # 1800

print("거스름돈은 ", ret1, "입니다.")

# 방법2
def solution(price2, money2):
    answer = 0
    result = 0
    result = sum(price2)

    if result > money2:  # 구매금액이 내가 가지고있는 금액보다 크다면
        return -1
    else:  # 구매금액보다 내가 가지고 있는 금액이 크다면
        answer = money2 - result
        return answer


price2 = [2100, 3200, 2100, 800]
money2 = 10000
ret2 = solution(price2, money2)  # 1800

print("거스름돈은 ", ret2, "입니다.")


# k번째로 작은 수
def solution(arr, k):
    list = []
    for i in arr:
        list += i
    list.sort()
    return list[k-1]

arr = [[5,12,4,31],[24,13,11,2],[43,44,19,26],[33,65,20,21]]
k = 4
ret = solution(arr, k)

print(ret)
