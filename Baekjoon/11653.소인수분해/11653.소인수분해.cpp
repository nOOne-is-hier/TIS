// 11653 – 소인수분해
// https://www.acmicpc.net/problem/11653
// solved.ac: https://solved.ac/search?query=11653
// 시간 제한: 1 초
// 메모리 제한: 256 MB
// 티어: 🟫 Bronze I
// 태그: 소수 판정, 소인수분해, 수학, 정수론
// 푼 사람 수: 60,318
// 평균 시도: 1.84

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

  int N;
  cin >> N;

  auto prime_factorization = [&](auto &&self) -> void
  {
    for (int i = 2; i <= N; ++i)
    {
      if (N % i == 0)
      {
        cout << i << '\n';
        N /= i;
        self(self);
        break;
      }
    }
  };

  prime_factorization(prime_factorization);

  return 0;
}
