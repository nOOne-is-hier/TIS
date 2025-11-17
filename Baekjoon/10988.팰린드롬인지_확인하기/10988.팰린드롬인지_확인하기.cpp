// 10988 – 팰린드롬인지 확인하기
// https://www.acmicpc.net/problem/10988
// solved.ac: https://solved.ac/search?query=10988
// 시간 제한: 1 초
// 메모리 제한: 256 MB
// 티어: 🟫 Bronze III
// 태그: 구현, 문자열
// 푼 사람 수: 61,739
// 평균 시도: 1.64

#include <algorithm>
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

  string S, R;
  cin >> S;
  R = S;
  reverse(R.begin(), R.end());

  cout << (S == R ? 1 : 0);

  return 0;
}
