#include <iostream>

using namespace std;

int dnq(long long A, long long B, long long C)
{
    if (B == 1)
        return A % C;
    long long half = dnq(A, B / 2, C);
    long long result = (half * half) % C;

    if (B % 2 == 1)
        result = (result * A) % C;

    return result;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long A, B, C;
    cin >> A >> B >> C;

    cout << dnq(A, B, C);

    return 0;
}
