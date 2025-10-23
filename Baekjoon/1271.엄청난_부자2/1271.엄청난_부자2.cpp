// 1271 – 엄청난 부자2
// https://www.acmicpc.net/problem/1271
// solved.ac: https://solved.ac/search?query=1271
// 시간 제한: 2 초
// 메모리 제한: 128 MB
// 티어: 🟫 Bronze V
// 태그: 사칙연산, 수학, 임의 정밀도 / 큰 수 연산
// 푼 사람 수: 26,414
// 평균 시도: 2.83

#include <algorithm>
#include <iostream>
#if defined(_WIN32)
#include <io.h>
#include <cstdio>
#else
#include <unistd.h>
#include <cstdio>
#endif

using namespace std;

string strip(const string &s)
{
  size_t i = 0;
  while (i + 1 < s.size() && s[i] == '0')
    ++i;
  return s.substr(i);
}
int cmp(const string &a_, const string &b_)
{
  string a = strip(a_), b = strip(b_);
  if (a.size() != b.size())
    return a.size() < b.size() ? -1 : 1;
  if (a == b)
    return 0;
  return a < b ? -1 : 1;
}
string mul1(const string &a_, int d)
{ // a * (0..9)
  if (d == 0)
    return "0";
  string a = string(a_.rbegin(), a_.rend());
  string res;
  int carry = 0;
  for (char c : a)
  {
    int x = (c - '0') * d + carry;
    res.push_back(char('0' + (x % 10)));
    carry = x / 10;
  }
  while (carry)
  {
    res.push_back(char('0' + (carry % 10)));
    carry /= 10;
  }
  while (res.size() > 1 && res.back() == '0')
    res.pop_back();
  reverse(res.begin(), res.end());
  return strip(res);
}
string sub(const string &a_, const string &b_)
{ // a >= b 가정, a-b
  string a = string(a_.rbegin(), a_.rend());
  string b = string(b_.rbegin(), b_.rend());
  string res;
  int carry = 0;
  for (size_t i = 0; i < a.size(); ++i)
  {
    int x = (a[i] - '0') - carry - (i < b.size() ? (b[i] - '0') : 0);
    if (x < 0)
    {
      x += 10;
      carry = 1;
    }
    else
      carry = 0;
    res.push_back(char('0' + x));
  }
  while (res.size() > 1 && res.back() == '0')
    res.pop_back();
  reverse(res.begin(), res.end());
  return strip(res);
}

pair<string, string> divmod_big(const string &A, const string &B)
{ // (quotient, remainder)
  string a = strip(A), b = strip(B);
  // 문제 조건상 b != "0" 가정
  if (cmp(a, b) < 0)
    return {"0", a};

  string q;
  q.reserve(a.size());
  string cur = "0";
  for (char ch : a)
  {
    if (cur == "0")
      cur = string(1, ch);
    else
      cur.push_back(ch);
    cur = strip(cur);

    // 다음 자릿수 찾기: 0..9 중 최대 d s.t. b*d <= cur
    int lo = 0, hi = 9, best = 0;
    while (lo <= hi)
    {
      int mid = (lo + hi) / 2;
      string prod = mul1(b, mid);
      int c = cmp(prod, cur);
      if (c <= 0)
      {
        best = mid;
        lo = mid + 1;
      }
      else
        hi = mid - 1;
    }
    q.push_back(char('0' + best));
    if (best > 0)
      cur = sub(cur, mul1(b, best));
    // else cur 그대로
  }
  return {strip(q), strip(cur)};
}

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

  string n, m;
  cin >> n >> m; // 매우 큰 수도 문자열로 안전
  auto [quo, rem] = divmod_big(n, m);
  cout << quo << '\n'
       << rem << '\n';
  return 0;
}
