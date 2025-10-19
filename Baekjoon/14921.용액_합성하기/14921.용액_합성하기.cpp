// 14921 – 용액 합성하기
// https://www.acmicpc.net/problem/14921
// solved.ac: https://solved.ac/search?query=14921
// 시간 제한: 1 초
// 메모리 제한: 512 MB
// 티어: 🟡 Gold V
// 태그: 두 포인터
// 푼 사람 수: 2,919
// 평균 시도: 2.14

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

  int N;
  cin >> N;
  vector<int> liquids(N);
  for (int &liquid : liquids)
    cin >> liquid;

  vector<int> pluses;
  pluses.reserve(N);
  vector<int> minuses;
  minuses.reserve(N);

  for (int &liquid : liquids)
    if (liquid < 0)
      minuses.push_back(liquid);
    else
      pluses.push_back(liquid);

  int result = 2e8 + 1;

  for (int i = 0; i < minuses.size(); ++i)
  {
    vector<int> candidates;
    if (i != minuses.size() - 1)
      candidates.push_back(minuses.back());

    if (!pluses.empty())
    {
      auto it = lower_bound(pluses.begin(), pluses.end(), abs(minuses[i]));
      if (it != pluses.end())
        candidates.push_back(*it);
      if (it != pluses.begin())
        candidates.push_back(*prev(it));
    }

    for (int &candidate : candidates)
      if (abs(result) > abs(minuses[i] + candidate))
        result = minuses[i] + candidate;
  }

  for (int i = 0; i < pluses.size(); ++i)
  {
    vector<int> candidates;
    if (i != 0)
      candidates.push_back(pluses[0]);

    if (!minuses.empty())
    {
      auto it = lower_bound(minuses.begin(), minuses.end(), -pluses[i]);
      if (it != minuses.end())
        candidates.push_back(*it);
      if (it != minuses.begin())
        candidates.push_back(*prev(it));
    }

    for (int &candidate : candidates)
      if (abs(result) > abs(pluses[i] + candidate))
        result = pluses[i] + candidate;
  }

  cout << result;

  return 0;
}
