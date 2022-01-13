# 모의고사 3회

# 01 거리 차이를 구하는 함수 빈칸 채우기
# diff = (b-a) if a < b else a-b


# 02 예산을 배분하기 위한 금액을 구하는 함수 빈칸 채우기
# 1. func_a(arr)
# 2. result.append(total // len(arr))
# 3. result.append(i)


# 03 가장 많이 같은 반을 보낸 학생을 찾는 함수 작성하기
def solution(table):
    answer = 0
    max = 0
    for i in range(1, len(table)):  # g\행 (학생)
        sum = 0
        for k in range(5):  # 열 (학년)
            teacher = table[0][k]
            student = table[i][k]
            if teacher == student:
                sum += 1
        if max < sum:
            max = sum
            print(i, "번 학생이 선생님과 가장 많이 같은 반")
            answer = i
    return answer


