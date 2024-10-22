'''
테스트 1 〉	통과 (0.38ms, 10.3MB)
테스트 2 〉	통과 (0.22ms, 10.3MB)
테스트 3 〉	통과 (0.24ms, 10.2MB)
테스트 4 〉	통과 (6.01ms, 10.5MB)
테스트 5 〉	통과 (6.36ms, 10.6MB)
테스트 6 〉	통과 (31.01ms, 12.8MB)
테스트 7 〉	통과 (75.08ms, 14.4MB)
테스트 8 〉	통과 (80.42ms, 14.2MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.03ms, 10.2MB)
테스트 11 〉	통과 (0.05ms, 10.1MB)
테스트 12 〉	통과 (0.03ms, 10.4MB)
테스트 13 〉	통과 (0.01ms, 10.3MB)
테스트 14 〉	통과 (0.05ms, 10.2MB)
테스트 15 〉	통과 (0.01ms, 10.4MB)
테스트 16 〉	통과 (0.04ms, 10.2MB)
테스트 17 〉	통과 (0.10ms, 10.3MB)
테스트 18 〉	통과 (0.02ms, 10.2MB)
테스트 19 〉	통과 (0.04ms, 10.4MB)
테스트 20 〉	통과 (89.28ms, 13.3MB)
테스트 21 〉	통과 (10.35ms, 10.4MB)
테스트 22 〉	통과 (76.44ms, 12.7MB)
테스트 23 〉	통과 (94.21ms, 12.2MB)
테스트 24 〉	통과 (108.53ms, 14MB)
테스트 25 〉	통과 (6.24ms, 10.4MB)
테스트 26 〉	통과 (26.19ms, 11.4MB)
테스트 27 〉	통과 (72.10ms, 11.9MB)
테스트 28 〉	통과 (7.94ms, 10.5MB)
테스트 29 〉	통과 (13.52ms, 10.9MB)
테스트 30 〉	통과 (48.48ms, 11.3MB)
테스트 31 〉	통과 (129.58ms, 13.5MB)
테스트 32 〉	통과 (9.12ms, 10.3MB)
테스트 33 〉	통과 (85.62ms, 12MB)
테스트 34 〉	통과 (116.26ms, 14MB)
테스트 35 〉	통과 (7.48ms, 10.3MB)
테스트 36 〉	통과 (53.22ms, 11.5MB)
테스트 37 〉	통과 (2.60ms, 10.2MB)
테스트 38 〉	통과 (2.00ms, 10.3MB)
테스트 39 〉	통과 (107.90ms, 13.2MB)
'''
def solution_with_gaps(distance, rocks, n):
    rocks.sort()  # 바위를 정렬합니다.
    rocks = [0] + rocks + [distance]  # 시작점과 마지막 도착 지점을 추가합니다.

    gaps = [rocks[i] - rocks[i - 1] for i in range(1, len(rocks))]  # 각 바위 사이의 거리 계산

    start, end = 0, distance  # 시작과 끝 범위를 설정합니다.
    answer = 0

    while start <= end:
        mid = (start + end) // 2
        current_gap = 0
        removed_rocks = 0

        for gap in gaps:
            current_gap += gap
            if current_gap < mid:
                removed_rocks += 1  # mid 값을 만족하지 못하면 바위를 제거합니다.
            else:
                current_gap = 0  # 만족하는 경우 현재 간격을 초기화합니다.

            if removed_rocks > n:
                break

        if removed_rocks > n:
            end = mid - 1  # mid 값을 줄여야 합니다.
        else:
            answer = mid  # 가능한 경우 답을 갱신하고
            start = mid + 1  # 더 큰 최소 거리를 탐색합니다.

    return answer

# 예시 테스트
distance = 25
rocks = [2, 14, 11, 21, 17]
n = 2
print(solution_with_gaps(distance, rocks, n))  # 투 포인터 풀이
