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

    int sum = 0;

    for (int i = 0; i <= N; ++i)
        for (int j = i; j <= N; ++j)
            sum += i + j;

    cout << sum;

    return 0;
}
