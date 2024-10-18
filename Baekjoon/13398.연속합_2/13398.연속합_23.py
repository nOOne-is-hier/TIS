# 입력과 출력을 처리하는 메인 함수
import sys

sys.stdin = open('input.txt')
class SegmentTree:
    def __init__(self, array):
        self.n = len(array)
        self.tree = [None] * (4 * self.n)
        self.build(array, 0, 0, self.n - 1)

    def build(self, array, node, start, end):
        if start == end:
            value = array[start]
            self.tree[node] = (value, value, value, value)  # (total, left max, right max, max sum)
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            self.build(array, left_child, start, mid)
            self.build(array, right_child, mid + 1, end)
            self.tree[node] = self.merge(self.tree[left_child], self.tree[right_child])

    def merge(self, left, right):
        total_sum = left[0] + right[0]
        left_max_sum = max(left[1], left[0] + right[1])
        right_max_sum = max(right[2], right[0] + left[2])
        max_sum = max(left[3], right[3], left[2] + right[1])
        return (total_sum, left_max_sum, right_max_sum, max_sum)

    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return (-float('inf'), -float('inf'), -float('inf'), -float('inf'))  # Invalid range, neutral element
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        left_result = self.query(left_child, start, mid, l, r)
        right_result = self.query(right_child, mid + 1, end, l, r)
        return self.merge(left_result, right_result)

# 입력과 출력을 처리하는 메인 함수
if __name__ == "__main__":
    N = int(input())
    array = list(map(int, input().split()))

    # 세그먼트 트리 생성
    segment_tree = SegmentTree(array)

    # 전체 구간에서의 최대 부분합 구하기
    result = segment_tree.query(0, 0, N - 1, 0, N - 1)[3]

    # 결과 출력
    print(result)
