#include <iostream>
#include <vector>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    vector<int> sequence(N);
    for (int &term : sequence)
        cin >> term;

    vector<int> dp;

    for (int i = 0; i < N; ++i)
        if (dp.empty() || sequence[i] > dp.back())
            dp.push_back(sequence[i]);

        else
            *lower_bound(dp.begin(), dp.end(), sequence[i]) = sequence[i];

    cout << dp.size() << '\n';

    return 0;
}
