# 모의고사 5회

# 01 도착지까지 충전 횟수를 구하는 함수 작성하기
def solution(arr):
    answer = 0
    energy = 40
    for i in arr:
        if energy < i:  # 남은 에너지로 i만큼 갈 수 있나?
            print(energy, "로", i, "만큼 못가요")
            energy = 40  # 충전
            answer += 1  # 충전 횟수
        energy -= i  # 다음 도시로 이동
    return answer

arr = [20, 10, 30, 30, 20, 10]
ret = solution(arr)
print(ret)


