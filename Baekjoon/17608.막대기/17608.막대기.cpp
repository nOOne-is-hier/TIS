// 17608 – 막대기
// https://www.acmicpc.net/problem/17608
// solved.ac: https://solved.ac/search?query=17608
// 시간 제한: 1 초 (추가 시간 없음)
// 메모리 제한: 512 MB
// 티어: 🟫 Bronze II
// 태그: 구현, 스택, 자료 구조
// 푼 사람 수: 11,988
// 평균 시도: 2.33

#include <iostream>
#include <stack>
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

  int N, h;

  cin >> N;

  stack<int> stack;

  while (N--)
  {
    cin >> h;
    stack.push(h);
  }

  int highest = 0;
  int seen = 0;
  while (stack.size())
  {
    if (highest < stack.top())
    {
      highest = stack.top();
      ++seen;
    }
    stack.pop();
  }

  cout << seen;

  return 0;
}
