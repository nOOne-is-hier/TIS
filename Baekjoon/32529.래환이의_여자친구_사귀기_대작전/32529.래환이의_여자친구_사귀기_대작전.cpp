// 32529 – 래환이의 여자친구 사귀기 대작전
// https://www.acmicpc.net/problem/32529
// solved.ac: https://solved.ac/search?query=32529
// 시간 제한: 1 초
// 메모리 제한: 1024 MB
// 티어: 🟫 Bronze II
// 태그: 구현
// 푼 사람 수: 273
// 평균 시도: 1.98

#include <iostream>
#include <vector>
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

  int N, M;
  cin >> N >> M;
  vector<int> diets(N);
  for (int &diet : diets)
    cin >> diet;

  int possible = 0;
  for (int i = N - 1; i >= 0; --i)
  {
    possible += diets[i];
    if (possible >= M)
    {
      cout << i + 1;
      exit(0);
    }
  }

  cout << -1;

  return 0;
}
