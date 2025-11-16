// 4999 – 아!
// https://www.acmicpc.net/problem/4999
// solved.ac: https://solved.ac/search?query=4999
// 시간 제한: 1 초
// 메모리 제한: 128 MB
// 티어: 🟫 Bronze V
// 태그: 구현, 문자열
// 푼 사람 수: 17,081
// 평균 시도: 1.60

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

  string A, B;
  cin >> A >> B;
  cout << (A.length() >= B.length() ? "go" : "no");
  return 0;
}
