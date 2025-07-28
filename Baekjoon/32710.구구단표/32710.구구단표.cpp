#include <iostream>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    bool sieve[101];
    fill(begin(sieve), end(sieve), false);

    for (int i = 1; i <= 9; ++i)
        for (int j = 1; j <= 9; ++j)
            sieve[i * j] = true;

    cout << sieve[N];

    return 0;
}
