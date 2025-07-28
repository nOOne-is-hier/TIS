#include <iostream>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int M;
    cin >> M;

    int T = 0;
    float real = 0;

    while (M)
    {
        --M, ++T;
        real += (T <= 30) ? 0.5 : 1.5;
    }

    cout.precision(1);
    cout << fixed << real;

    return 0;
}
