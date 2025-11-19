// 2745 – 진법 변환
// https://www.acmicpc.net/problem/2745
// solved.ac: https://solved.ac/search?query=2745
// 시간 제한: 1 초
// 메모리 제한: 128 MB
// 티어: 🟫 Bronze II
// 태그: 구현, 문자열, 수학
// 푼 사람 수: 36,879
// 평균 시도: 2.04

#include <cmath>
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

  string N;
  int B;
  cin >> N >> B;

  int val = 0;
  for (int i = 0; i < N.length(); ++i)
    val += (isdigit(N[i]) ? N[i] - '0' : N[i] - 'A' + 10) * pow(B, N.length() - i - 1);

  cout << val;

  return 0;
}
