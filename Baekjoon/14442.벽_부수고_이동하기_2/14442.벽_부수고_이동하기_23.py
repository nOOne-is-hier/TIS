import sys
import heapq

# 델타 배열 (상하좌우 이동)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


# 맨해튼 거리 함수 (현재 위치와 목표 위치 사이의 거리)
def manhattan_dist(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)


def a_star(N, M, K, game_map):
    # 우선순위 큐 (heapq 사용), 시작점은 (0, 0)에서 시작
    pq = []
    heapq.heappush(pq, (0 + manhattan_dist(0, 0, N - 1, M - 1), 0, 0, 0, 0))  # (f(n), g(n), row, column, 부순 벽 수)

    # 방문 여부를 비트마스크로 관리 (각 좌표에 대해 벽을 부순 횟수를 기록)
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1 << 0  # 시작점에서 벽을 부수지 않고 방문 처리

    while pq:
        # 가장 비용이 적은 상태를 가져옴
        f, g, r, c, broken_blocks = heapq.heappop(pq)

        # 종료 조건: 도착 지점에 도착하면 종료
        if r == N - 1 and c == M - 1:
            return g + 1  # 시작점도 포함해야 하므로 +1

        # 4방향으로 이동
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            # 맵의 범위를 벗어나지 않고, 이전 상태를 재탐색하지 않도록 조건 추가
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] & ((1 << broken_blocks + 1) - 1):
                # 빈 칸(0)을 이동하는 경우
                if game_map[nr][nc] == 0:
                    visited[nr][nc] |= (1 << broken_blocks)  # 벽을 부수지 않은 경우 방문 처리
                    new_g = g + 1
                    h = manhattan_dist(nr, nc, N - 1, M - 1)
                    heapq.heappush(pq, (new_g + h, new_g, nr, nc, broken_blocks))

                # 벽일 경우, 벽을 부술 수 있다면
                elif game_map[nr][nc] == 1 and broken_blocks < K and not (visited[nr][nc] & (1 << (broken_blocks + 1))):
                    visited[nr][nc] |= (1 << (broken_blocks + 1))  # 벽을 부수고 방문 처리
                    new_g = g + 1
                    h = manhattan_dist(nr, nc, N - 1, M - 1)
                    heapq.heappush(pq, (new_g + h, new_g, nr, nc, broken_blocks + 1))

    # 만약 도착할 수 없다면 -1 반환
    return -1


# 메인 함수
def main():
    input_data = sys.stdin.read().splitlines()  # 한 번에 모든 입력을 받음
    N, M, K = map(int, input_data[0].split())  # 첫 번째 줄에서 N, M, K 읽음
    game_map = [list(map(int, line)) for line in input_data[1:]]  # 그 다음 줄부터 게임 맵 읽음

    # A* 알고리즘 수행
    result = a_star(N, M, K, game_map)

    # 결과 출력
    sys.stdout.write(str(result) + '\n')


# 입력 처리
sys.stdin = open('input.txt')
main()
