# 모의고사 4회

# 01 카드 숫자 조합하여 홀수의 개수를 구하는 함수 빈칸 채우기
# 1. i + 1
# 2. k + 1


# 02 무게를 재기 위해 필요한 추의 개수를 구하는 함수 빈칸 채우기
# 1. arr.sort()  # 크기 순으로 정렬
# 2. diff = payload - weight


# 03 통학버스 왕복 횟수 구하는 함수 작성하기
def solution(student, apts):
    result = 0
    total = 0
    for i in student:
        total += i
    result = total // 12
    if total % 12 != 0:
        result += 1
    return result
