// 11948 – 과목선택
// https://www.acmicpc.net/problem/11948
// solved.ac: https://solved.ac/search?query=11948
// 시간 제한: 2 초
// 메모리 제한: 512 MB
// 티어: 🟫 Bronze IV
// 태그: 구현, 사칙연산, 수학
// 푼 사람 수: 7,453
// 평균 시도: 1.33

#include <algorithm>
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

  int A, B, C, D, E, F;
  cin >> A >> B >> C >> D >> E >> F;
  vector<int> sciences = {A, B, C, D};
  int total = A + B + C + D + E + F;
  total -= *min_element(sciences.begin(), sciences.end()) + min(E, F);
  cout << total;
  return 0;
}
