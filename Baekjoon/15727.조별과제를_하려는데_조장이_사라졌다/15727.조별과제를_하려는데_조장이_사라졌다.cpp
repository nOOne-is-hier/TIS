// 15727 – 조별과제를 하려는데 조장이 사라졌다
// https://www.acmicpc.net/problem/15727
// solved.ac: https://solved.ac/search?query=15727
// 시간 제한: 1 초
// 메모리 제한: 128 MB
// 티어: 🟫 Bronze V
// 태그: 사칙연산, 수학
// 푼 사람 수: 11,966
// 평균 시도: 1.62

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

  int L;
  cin >> L;
  cout << (L % 5 ? L / 5 + 1 : L / 5);
  return 0;
}
