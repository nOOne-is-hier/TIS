// 11942 – 고려대는 사랑입니다
// https://www.acmicpc.net/problem/11942
// solved.ac: https://solved.ac/search?query=11942
// 시간 제한: 1 초
// 메모리 제한: 32 MB
// 티어: 🟫 Bronze V
// 태그: 구현
// 푼 사람 수: 21,492
// 평균 시도: 1.15

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

  cout << "고려대학교";
  return 0;
}
