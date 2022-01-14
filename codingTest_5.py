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
# def solution(arr):
#     answer = 0
#     for i in range(len(arr)):
#         price = arr[i]  # 가격
#         if (i+1) % 4 == 0:  # 4번째는 반 값
#             price //= 2  # 반 값으로
#         answer += price
#     return answer
#
#
# arr = [100, 500, 200, 400, 300]
# ret = solution(arr)
# print(ret)


# 03 목재소의 매출액을 구하는 함수 수정하기
# def func_a(a, length):
#     for i in range(len(a)):
#         if a[i] >= length:
#             return i
#     return -1
#
#
# def solution(N, orders):
#     material = [8 for _ in range(N)]  # 초기값은 8 이어야 한다
#     # 8로 초기화한 8개 방이 만들어짐 [8, 8, 8, 8, 8, 8, 8, 8]
#     k = 0
#     price = 0
#     for o in orders:
#         # print(material)
#         k = func_a(material, o)
#         if k >= 0:
#             material[k] -= o
#             price += 3000 * o
#     return price
#
#
# orders = [1, 3, 5, 7, 8]
# ret = solution(8, orders)
# print(ret)


# 04 영문 단어를 전화번호로 변환하는 함수 수정하기
def solution(word):
    num2alpha = ["oqz", "ij", "abc", "def", "gh", "kl", "mn", "prs", "tuv", "wxy"]
    answer = ' '
    for c in word:
        for i in range(len(num2alpha)):
            for a in num2alpha[i]:
                if a == c:     # 비교 문자는 c
                    answer += str(i)
                    break
    return answer


word = 'whitepawn'  # 941837296
ret = solution(word)
print(ret)
