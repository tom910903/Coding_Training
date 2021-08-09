def solution(N, stages):
    answer = {}
    num = len(stages)

    for i in range(1,N+1):
        if num != 0:
            count = stages.count(i)
            answer[i] = count / num
            num -= count
        else:
            answer[i] = 0

    return sorted(answer, key=lambda x : answer[x], reverse=True)