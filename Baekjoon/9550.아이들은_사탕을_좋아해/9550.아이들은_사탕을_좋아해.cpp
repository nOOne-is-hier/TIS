// 9550 – 아이들은 사탕을 좋아해
// https://www.acmicpc.net/problem/9550
// solved.ac: https://solved.ac/search?query=9550
// 시간 제한: 1 초
// 메모리 제한: 128 MB
// 티어: 🟫 Bronze III
// 태그: 사칙연산, 수학
// 푼 사람 수: 3,172
// 평균 시도: 1.19

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

  int T;
  cin >> T;
  while (T--)
  {
    int N, K;
    cin >> N >> K;
    int max_child = 0;
    while (N--)
    {
      int candy;
      cin >> candy;
      max_child += candy / K;
    }
    cout << max_child << '\n';
  }
  return 0;
}
