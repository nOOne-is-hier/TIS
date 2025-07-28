#include <iostream>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int A, B, K, X;
    cin >> A >> B >> K >> X;

    cout << (((K + X <= B ? K + X : B) - (K - X >= A ? K - X : A) + 1 > 0) ? to_string((K + X <= B ? K + X : B) - (K - X >= A ? K - X : A) + 1) : "IMPOSSIBLE");

    return 0;
}
