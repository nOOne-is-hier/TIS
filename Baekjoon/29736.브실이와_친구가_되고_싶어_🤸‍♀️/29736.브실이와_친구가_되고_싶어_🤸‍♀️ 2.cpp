#include <iostream>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int A, B, K, X;
    cin >> A >> B >> K >> X;

    int result = min(B, K + X) - max(K - X, A) + 1;

    cout << (result > 0 ? to_string(result) : "IMPOSSIBLE");

    return 0;
}
