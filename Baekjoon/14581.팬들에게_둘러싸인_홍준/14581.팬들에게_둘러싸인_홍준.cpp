// 14581 – 팬들에게 둘러싸인 홍준
// https://www.acmicpc.net/problem/14581
// solved.ac: https://solved.ac/search?query=14581
// 시간 제한: 1 초
// 메모리 제한: 64 MB
// 티어: 🟫 Bronze V
// 태그: 구현
// 푼 사람 수: 9,515
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

  string id;
  cin >> id;
  cout << ":fan::fan::fan:\n:fan::" << id << "::fan:\n:fan::fan::fan:";
  return 0;
}
