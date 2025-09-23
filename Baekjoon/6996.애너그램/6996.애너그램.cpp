// 6996 – 애너그램
// https://www.acmicpc.net/problem/6996
// solved.ac: https://solved.ac/search?query=6996
// 시간 제한: 1 초
// 메모리 제한: 128 MB
// 티어: 🟫 Bronze I
// 태그: 구현, 문자열, 정렬
// 푼 사람 수: 4,364
// 평균 시도: 1.93

#include <iostream>
#include <unordered_map>
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

  int T;
  cin >> T;
  while (T--)
  {
    string A, B;
    unordered_map<char, int> la, lb;
    cin >> A >> B;
    for (char &c : A)
      ++la[c];
    for (char &c : B)
      ++lb[c];

    cout << A << " & " << B << " are " << (la == lb ? "" : "NOT ") << "anagrams." << '\n';
  }
  return 0;
}
