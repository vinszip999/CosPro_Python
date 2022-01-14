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
# def solution(word):
#     num2alpha = ["oqz", "ij", "abc", "def", "gh", "kl", "mn", "prs", "tuv", "wxy"]
#     answer = ' '
#     for c in word:
#         for i in range(len(num2alpha)):
#             for a in num2alpha[i]:
#                 if a == c:     # 비교 문자는 c
#                     answer += str(i)
#                     break
#     return answer
#
#
# word = 'whitepawn'  # 941837296
# ret = solution(word)
# print(ret)


# 05 주차장 요금 정산하는 함수 빈칸 채우기
# def func_a(a):
#     #             시간             분
#     return ((a // 100) * 60) + (a % 100)
#
#
# def solution(arr):
#     answer = 0
#     # 마감시간
#     min_a = func_a(2200)  # 밤 10시 : 2200
#     for i in arr:
#         # 들어오는 시간
#         min_b = func_a(i)  # 차량이 들어온 시간
#         elapsed_minute = min_a - min_b
#         answer += 1000 + (elapsed_minute // 10) * 500
#     return answer
#
#
# arr = [2200, 2200]
# ret = solution(arr)
# print(ret)


# 06 KTX 열차 승차 인원 구하는 함수 빈칸 채우기
# up : 타는 사람, down : 내리는 사람
# def solution(down, up):
#     answer = 0
#     passenger = 0
#     n = len(down)  # len(up) 가능
#     for i in range(n):
#         passenger += up[i] - down[i]  # 탑승인원
#         stand = passenger - 240  # 입석 = 탑승명 - 좌석수
#         if stand < 0:  # 입석 없을 경우
#             stand = 0
#         if stand > 0 and stand > answer:  # 최대 입석 수 저장
#             answer = stand
#         print(passenger, stand)
#     return answer
#
#
# up = [240, 100, 0, 160, 10, 140]
# down = [0, 0, 140, 80, 0, 0]
# ret = solution(down, up)
# print(ret)


# 07 판매 이익금을 구하는 함수 수정하기
# def func_a(a):
#     min = a[0]
#     for i in a:
#         if i < min:
#             min = i
#     return min
#
#
# def solution(price):
#     sales = [0 for _ in range(len(price))]
#     # print(sales)
#     for i in range(len(price)):
#         # * 이차원 배열이다 *
#         if price[i][0] < 5000:
#             percent = 0.25
#         elif price[i][0] < 15000:
#             percent = 0.20
#         elif price[i][0] < 100000:
#             percent = 0.15
#         else:
#             percent = 0.1
#
#         # sales[price.index(i)] = int(i[0] * percent * i[1])
#         sales[i] = int(price[i][0] * percent * price[i][1])
#         # ** 원가 * percent * 수량이다 ** / 금액 정수로 바꿔줌
#     return func_a(sales)
#
#
# price = [
#     [50000, 10],
#     [15000, 20],
#     [5000, 40],
#     [150000, 100]
# ]
# ret = solution(price)
# print(ret)


# 08 직선으로 교차하는 두 직선과 x축의 선이 이루는 삼각형 면적을 구하는 함수 작성하기
def solution(x, y):
    answer = 0
    b1 = y - x   # y = x+b1에서의 b1졀편
    b2 = y + x  # y = -x+b2에서의 b2졀편
    a1 = (y * (x - (-b1))) / 2.0  # y = x + b1에서  y=0 일 때  x값  -b1
    a2 = (y * (b2 - x)) / 2.0  # y = -x + b2에서 y=0 일 때 x값  b2
    answer = a1 + a2
    return answer


ret = solution(10, 4)
print(ret)
