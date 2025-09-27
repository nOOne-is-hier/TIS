// 2902 – KMP는 왜 KMP일까?
// https://www.acmicpc.net/problem/2902
// solved.ac: https://solved.ac/search?query=2902
// 시간 제한: 1 초
// 메모리 제한: 128 MB
// 티어: 🟫 Bronze III
// 태그: 구현, 문자열
// 푼 사람 수: 14,187
// 평균 시도: 1.21

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

  string line;
  cin >> line;

  for (int i = 0; i < line.length(); ++i)
    (i == 0 || line[i - 1] == '-') && cout << line[i];

  return 0;
}
