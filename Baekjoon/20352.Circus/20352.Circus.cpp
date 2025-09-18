// 20352 – Circus
// https://www.acmicpc.net/problem/20352
// solved.ac: https://solved.ac/search?query=20352
// 시간 제한: 2 초
// 메모리 제한: 512 MB
// 티어: 🟫 Bronze IV
// 태그: 기하학, 수학
// 푼 사람 수: 1,728
// 평균 시도: 1.24

#include <iostream>
#include <cmath>
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
  long long a;
  cin >> a;
  const long double PI = acosl(-1.0L);
  double r = sqrt(a / PI);
  cout << fixed << setprecision(9) << 2 * PI * r;
  return 0;
}
