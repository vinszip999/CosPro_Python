# 모의고사 3회

# 01 거리 차이를 구하는 함수 빈칸 채우기
# diff = (b-a) if a < b else a-b


# 02 예산을 배분하기 위한 금액을 구하는 함수 빈칸 채우기
# 1. func_a(arr)
# 2. result.append(total // len(arr))
# 3. result.append(i)


# 03 가장 많이 같은 반을 보낸 학생을 찾는 함수 작성하기
# def solution(table):
#     answer = 0
#     max = 0
#     for i in range(1, len(table)):  # g\행 (학생)
#         sum = 0
#         for k in range(5):  # 열 (학년)
#             teacher = table[0][k]
#             student = table[i][k]
#             if teacher == student:
#                 sum += 1
#         if max < sum:
#             max = sum
#             print(i, "번 학생이 선생님과 가장 많이 같은 반")
#             answer = i
#     return answer


# 04 페인트칠을 하는데 걸리는 시간을 구하는 함수 빈칸 채우기
# 1. hour // 2
# 2. hour // 4
# 3. answer = hour-1


# 05 카드 게임 승자 알아내는 함수 작성하기 **
# def solution(mho_cards, mhe_cards):
#     result = -1
#     minho = 0
#     minhee = 0
#     for i in range(len(mho_cards)):
#         if mho_cards[i] > mhe_cards[i]:
#             minho += 1
#         elif mho_cards[i] < mhe_cards[i]:
#             minhee += 1
#     if minho > minhee:
#         result = 1
#     elif minho < minhee:
#         result = 0
#     else:  # minho == minhee:
#         result = -1
#     return result


# 06 문자열 내 정수들의 총합을 구하는 함수 빈칸 채우기
# 1. '0' <= c
# 2. c <= '9'
# 3. number * 10


# 07 야구 게임의 볼 판정 함수 수정하기
# b //= 10
# -->
# a //= 10  # b가 아니라 a


# 08 문자열 내에 지정하는 문자들이 있는지 확인하는 함수 수정하기
# if match_cnt >= len(password):
# -->
# if match_cnt >= len(key):  # key의 길이와 같아야 함

# 09 A,B,C,D 4개의 각 축구팀의 총 승점을 구하는 함수 수정하기
# result[i] += scores[i][k]
# -->
# result[i] += scores[i][k]*2  # 승리 시 승점은 2점

# 10 문자열들을 처리하는 시간 구하는 함수 수정하기
# if length % 4 == 0:
# -->
# if length % 4 != 0:  # 남는 문자가 3개 이하일 때 한 번 처리
