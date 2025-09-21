// 3181 – 줄임말 만들기
// https://www.acmicpc.net/problem/3181
// solved.ac: https://solved.ac/search?query=3181
// 시간 제한: 1 초
// 메모리 제한: 128 MB
// 티어: 🟫 Bronze II
// 태그: 구현, 문자열
// 푼 사람 수: 1,405
// 평균 시도: 1.60

#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <string>
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

  string line, word;
  vector<string> useless = {"i", "pa", "te", "ni", "niti", "a", "ali", "nego", "no", "ili"};

  // 한 줄 입력
  getline(cin, line);
  stringstream ss(line);

  bool firstWord = true;
  while (ss >> word)
  {
    if (firstWord || find(useless.begin(), useless.end(), word) == useless.end())
    {
      cout << (char)toupper(word[0]);
    }
    firstWord = false;
  }
  return 0;
}
