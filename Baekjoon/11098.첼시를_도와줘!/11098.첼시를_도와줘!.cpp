// 11098 – 첼시를 도와줘!
// https://www.acmicpc.net/problem/11098
// solved.ac: https://solved.ac/search?query=11098
// 시간 제한: 1 초
// 메모리 제한: 256 MB
// 티어: 🟫 Bronze II
// 태그: 구현, 문자열
// 푼 사람 수: 6,830
// 평균 시도: 1.66

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

  int n;
  cin >> n;
  while (n--)
  {
    int p;
    cin >> p;
    int highest_price = 0;
    string most_worthy;
    while (p--)
    {
      int price;
      string name;
      cin >> price >> name;
      if (highest_price < price)
      {
        highest_price = price;
        most_worthy = name;
      }
    }
    cout << most_worthy << '\n';
  }
  return 0;
}
