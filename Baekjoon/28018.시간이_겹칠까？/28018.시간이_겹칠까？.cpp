// 28018 – 시간이 겹칠까?
// https://www.acmicpc.net/problem/28018
// solved.ac: https://solved.ac/search?query=28018
// 시간 제한: 1 초
// 메모리 제한: 512 MB
// 티어: 🟡 Gold V
// 태그: 누적 합, 차분 배열 트릭
// 푼 사람 수: 530
// 평균 시도: 2.49

#include <iostream>
#include <vector>
#if defined(_WIN32)
#include <io.h>
#include <cstdio>
#else
#include <unistd.h>
#include <cstdio>
#endif

using namespace std;

int main()
{
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  // 표준입력이 터미널이면 input.txt로 대체 (파이프 입력 시에는 그대로 cin)
#if defined(_WIN32)
  if (_isatty(_fileno(stdin)))
  {
    freopen("input.txt", "r", stdin);
  }
#else
  if (isatty(fileno(stdin)))
  {
    freopen("input.txt", "r", stdin);
  }
#endif

  int N;
  cin >> N;
  vector<int> time_table(1e6 + 2, 0);

  while (N--)
  {
    int S, E;
    cin >> S >> E;
    ++time_table[S];
    --time_table[E + 1];
  }

  for (int i = 1; i < 1e6 + 1; ++i)
    time_table[i] += time_table[i - 1];

  int Q;
  cin >> Q;
  while (Q--)
  {
    int time;
    cin >> time;
    cout << time_table[time] << '\n';
  }

  return 0;
}
