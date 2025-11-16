// 2444 – 별 찍기 - 7
// https://www.acmicpc.net/problem/2444
// solved.ac: https://solved.ac/search?query=2444
// 시간 제한: 1 초
// 메모리 제한: 128 MB
// 티어: 🟫 Bronze III
// 태그: 구현
// 푼 사람 수: 67,094
// 평균 시도: 1.80

#include <iostream>
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

  auto print = [&](auto &&self, int cnt) -> void
  {
    for (int i = 0; i < N - cnt; ++i)
      cout << ' ';

    for (int i = 0; i < cnt * 2 - 1; ++i)
      cout << '*';

    cout << '\n';

    if (cnt == N)
      return;

    self(self, cnt + 1);

    for (int i = 0; i < N - cnt; ++i)
      cout << ' ';

    for (int i = 0; i < cnt * 2 - 1; ++i)
      cout << '*';

    cout << '\n';
  };

  print(print, 1);

  return 0;
}
