'''
통과 (0.19ms, 10.2MB)
테스트 2 〉	통과 (0.26ms, 10.1MB)
테스트 3 〉	통과 (0.22ms, 10.2MB)
테스트 4 〉	통과 (5.66ms, 10.4MB)
테스트 5 〉	통과 (5.60ms, 10.2MB)
테스트 6 〉	통과 (40.56ms, 12.7MB)
테스트 7 〉	통과 (66.46ms, 12.7MB)
테스트 8 〉	통과 (87.26ms, 12.6MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.02ms, 10.2MB)
테스트 11 〉	통과 (0.02ms, 10.2MB)
테스트 12 〉	통과 (0.03ms, 10.2MB)
테스트 13 〉	통과 (0.01ms, 10.2MB)
테스트 14 〉	통과 (0.03ms, 10.2MB)
테스트 15 〉	통과 (0.01ms, 10.3MB)
테스트 16 〉	통과 (0.03ms, 10.2MB)
테스트 17 〉	통과 (0.06ms, 10.2MB)
테스트 18 〉	통과 (0.01ms, 10.3MB)
테스트 19 〉	통과 (0.02ms, 10.2MB)
테스트 20 〉	통과 (64.65ms, 12.1MB)
테스트 21 〉	통과 (9.73ms, 10.2MB)
테스트 22 〉	통과 (68.06ms, 11.5MB)
테스트 23 〉	통과 (74.07ms, 11.3MB)
테스트 24 〉	통과 (77.31ms, 12.8MB)
테스트 25 〉	통과 (5.57ms, 10.5MB)
테스트 26 〉	통과 (23.73ms, 10.7MB)
테스트 27 〉	통과 (49.61ms, 11.2MB)
테스트 28 〉	통과 (6.94ms, 10.4MB)
테스트 29 〉	통과 (10.97ms, 10.6MB)
테스트 30 〉	통과 (50.17ms, 10.9MB)
테스트 31 〉	통과 (224.48ms, 12.1MB)
테스트 32 〉	통과 (9.41ms, 10.2MB)
테스트 33 〉	통과 (100.31ms, 11.3MB)
테스트 34 〉	통과 (128.96ms, 12.7MB)
테스트 35 〉	통과 (6.98ms, 10.4MB)
테스트 36 〉	통과 (49.01ms, 11MB)
테스트 37 〉	통과 (2.38ms, 10.2MB)
테스트 38 〉	통과 (1.68ms, 10MB)
테스트 39 〉	통과 (99.23ms, 12MB)
'''
import sys

sys.stdin = open('input.txt')


def solution(distance, rocks, n):
    sorted_rocks = sorted(rocks) + [distance]

    start, end = 0, distance
    answer = 0

    while start <= end:
        mid = (start + end) // 2
        current = 0
        removed_rocks = 0

        for rock in sorted_rocks:
            if rock - current < mid:
                removed_rocks += 1
            else:
                current = rock

            if removed_rocks > n:
                break

        if removed_rocks > n:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1

    return answer

print(solution(25, [2, 14, 11, 21, 17], 2))
