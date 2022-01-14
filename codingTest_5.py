# 모의고사 5회

# 01 도착지까지 충전 횟수를 구하는 함수 작성하기
# def solution(arr):
#     answer = 0
#     energy = 40
#     for i in arr:
#         if energy < i:  # 남은 에너지로 i만큼 갈 수 있나?
#             print(energy, "로", i, "만큼 못가요")
#             energy = 40  # 충전
#             answer += 1  # 충전 횟수
#         energy -= i  # 다음 도시로 이동
#     return answer
#
#
# arr = [20, 10, 30, 30, 20, 10]
# ret = solution(arr)
# print(ret)


# 02 3개 사면 추가 하나는 50% 할인 행사의 금액을 계산하는 함수 빈칸 채우기
def solution(arr):
    answer = 0
    for i in range(len(arr)):
        price = arr[i]  # 가격
        if (i+1) % 4 == 0:  # 4번째는 반 값
            price //= 2  # 반 값으로
        answer += price
    return answer


arr = [100, 500, 200, 400, 300]
ret = solution(arr)
print(ret)
