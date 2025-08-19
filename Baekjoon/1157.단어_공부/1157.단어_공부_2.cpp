// 1157 – 단어 공부
// https://www.acmicpc.net/problem/1157
// solved.ac: https://solved.ac/search?query=1157
// 시간 제한: 2 초
// 메모리 제한: 128 MB
// 티어: 🟫 Bronze I
// 태그: 구현, 문자열
// 푼 사람 수: 109,599
// 평균 시도: 2.48

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
    vector<int> dat(26);

    cin >> word;
    for (char l : word)
        ++dat[toupper(l) - 'A'];

    int max_val = *max_element(dat.begin(), dat.end());
    int cnt = count(dat.begin(), dat.end(), max_val);

    cout << (cnt > 1 ? '?' : (char)('A' + find(dat.begin(), dat.end(), max_val) - dat.begin()));
    return 0;
}
