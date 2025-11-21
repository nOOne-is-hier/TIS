// 11005 – 진법 변환 2
// https://www.acmicpc.net/problem/11005
// solved.ac: https://solved.ac/search?query=11005
// 시간 제한: 0.5 초 (추가 시간 없음)
// 메모리 제한: 256 MB
// 티어: 🟫 Bronze I
// 태그: 구현, 수학
// 푼 사람 수: 32,385
// 평균 시도: 2.15

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

  int N, B;
  cin >> N >> B;

  string result = "";

  while (N)
  {
    int a = N % B;
    N /= B;

    result = char(a < 10 ? a + '0' : a - 10 + 'A') + result;
  }

  cout << result;

  return 0;
}
