#include <iostream>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int M, F;

    while (cin >> M && cin >> F && M && F)
        cout << M + F << '\n';

    return 0;
}
