# 모의고사 4회

# 01 카드 숫자 조합하여 홀수의 개수를 구하는 함수 빈칸 채우기
# 1. i + 1
# 2. k + 1


# 02 무게를 재기 위해 필요한 추의 개수를 구하는 함수 빈칸 채우기
# 1. arr.sort()  # 크기 순으로 정렬
# 2. diff = payload - weight


# 03 통학버스 왕복 횟수 구하는 함수 작성하기
# def solution(student, apts):
#     result = 0
#     total = 0
#     for i in student:
#         total += i
#     result = total // 12
#     if total % 12 != 0:
#         result += 1
#     return result


# 04 열린 문의 개수를 구하는 함수 빈칸 채우기
# 1. range(m + 1)
# 2. 1 - room[k]  # 1-> 0, 0 -> 1
# 3. OPEN


# 05 대괄호 쌍의 개수를 세는 함수 빈칸 채우기
# 1. False
# 2. True


# 06 수업별 신청자 인원수 구하는 함수 수정하기
# answer[i] += arr[i+k]
# -->
# answer[i] += arr[i*4+k]  # 과목별로 4개씩


# 07 화면 내 이동 시 x와 y가 같은 위치 개수를 구하는 함수 수정하기
# answer += 1
# -->
# if x == y: answer += 1  # x, y가 같을 때의 개수이다


# 08 평균과 가장 큰 차이가 나는 점수 구하는 함수 수정하기
# return b if a < b else a
# -->
# return b - a if a < b else a - b  # 두 값의 차이 변환


# 09 단체 여행 숙소 방의 개수를 구하는 함수 수정하기
# answer += i
# -->
# answer += i//k  # answer는 방 개수, i는 각 학년의 인원 수


# 10 중간고사 폐지를 위한 설문조사 결과를 구하는 함수 작성하기
# def solution(positive, negative):
#     answer = [0, 0]
#     total = 0  # 찬성과 반대를 합한 총 인원 수
#     p_sum = 0  # 찬성 표의 총합
#     n_sum = 0  # 반대 표의 총합
#     for i in range(4):  # 학년
#         for k in range(3):  # 단과대
#             total += positive[i][k] + negative[i][k]
#             p_sum += positive[i][k]
#             n_sum += negative[i][k]
#     answer[0] = int(p_sum / total * 100)
#     answer[1] = int(n_sum / total * 100)
#     return answer
