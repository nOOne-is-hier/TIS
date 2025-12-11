// 29751 – 삼각형
// https://www.acmicpc.net/problem/29751
// solved.ac: https://solved.ac/search?query=29751
// 시간 제한: 0.1 초
// 메모리 제한: 1024 MB
// 티어: 🟫 Bronze V
// 태그: 기하학, 사칙연산, 수학
// 푼 사람 수: 5,859
// 평균 시도: 1.45

#include <iostream>
#include <iomanip>
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

  int W, H;
  cin >> W >> H;
  cout << fixed << setprecision(1) << W * H * 0.5;
  return 0;
}
