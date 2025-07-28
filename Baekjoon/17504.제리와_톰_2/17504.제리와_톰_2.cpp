#include <iostream>
#include <vector>

using namespace std;

pair<long long, long long> conbine(long long whole, long long denominator, long long numerator)
{
    return {denominator, whole * denominator + numerator};
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    vector<long long> sequence(N);

    for (int i = 0; i < N; ++i)
        cin >> sequence[i];

    long long numerator = 1;
    long long denominator = sequence[N - 1];
    for (int i = N - 1; i > 0; --i)
    {
        pair<long long, long long> mixed = conbine(sequence[i - 1], denominator, numerator);
        numerator = mixed.first;
        denominator = mixed.second;
    }

    cout << denominator - numerator << '\n'
         << denominator;

    return 0;
}
