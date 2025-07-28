#include <iostream>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int R, S;
    cin >> R >> S;

    int left = (R * 8) + (S * 3) - 28;

    cout << (left > 0 ? left : 0);

    return 0;
}
