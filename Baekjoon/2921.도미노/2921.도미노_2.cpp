// 도미노 (2921)
// https://www.acmicpc.net/problem/2921

#include <iostream>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;

    cin >> N;

    cout << 1LL * N * (N + 1) * (N + 2) / 2;

    return 0;
}
