// 10170 – NFC West vs North
// https://www.acmicpc.net/problem/10170
// solved.ac: https://solved.ac/search?query=10170
// 시간 제한: 1 초
// 메모리 제한: 256 MB
// 티어: 🟫 Bronze V
// 태그: 구현
// 푼 사람 수: 14,505
// 평균 시도: 1.33

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

  cout << "NFC West       W   L  T" << '\n';
  cout << "-----------------------" << '\n';
  cout << "Seattle        13  3  0" << '\n';
  cout << "San Francisco  12  4  0" << '\n';
  cout << "Arizona        10  6  0" << '\n';
  cout << "St. Louis      7   9  0" << '\n';
  cout << '\n';
  cout << "NFC North      W   L  T" << '\n';
  cout << "-----------------------" << '\n';
  cout << "Green Bay      8   7  1" << '\n';
  cout << "Chicago        8   8  0" << '\n';
  cout << "Detroit        7   9  0" << '\n';
  cout << "Minnesota      5  10  1" << '\n';
  return 0;
}
