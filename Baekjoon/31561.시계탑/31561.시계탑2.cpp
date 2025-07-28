#include <iostream>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int M;
    cin >> M;

    cout.precision(1);
    cout << fixed << 0.5f * min(30, M) + 1.5f * max(0, M - 30);

    return 0;
}
