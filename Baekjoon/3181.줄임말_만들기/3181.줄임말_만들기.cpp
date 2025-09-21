// 3181 – 줄임말 만들기
// https://www.acmicpc.net/problem/3181
// solved.ac: https://solved.ac/search?query=3181
// 시간 제한: 1 초
// 메모리 제한: 128 MB
// 티어: 🟫 Bronze II
// 태그: 구현, 문자열
// 푼 사람 수: 1,405
// 평균 시도: 1.60

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

  string word;
  vector<string> useless = {"i", "pa", "te", "ni", "niti", "a", "ali", "nego", "no", "ili"};
  bool firstWord = true;
  while (cin >> word)
  {
    if (firstWord || useless.end() == find(useless.begin(), useless.end(), word))
      cout << (char)toupper(word[0]);
    firstWord = false;
  }
  return 0;
}
