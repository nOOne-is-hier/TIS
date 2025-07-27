#include <algorithm>
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

    for (int &elem : sequence)
        cin >> elem;

    vector<int> temp;
    vector<int> result(N);

    for (int i = 0; i < N; ++i)
    {
        if (temp.empty() || temp.back() < sequence[i])
            temp.push_back(sequence[i]);

        else
            *lower_bound(temp.begin(), temp.end(), sequence[i]) = sequence[i];
        result[i] = temp.size();
    }

    temp.clear();
    int answer = 0;

    for (int i = N - 1; i >= 0; --i)
    {
        if (temp.empty() || temp.back() < sequence[i])
            temp.push_back(sequence[i]);

        else
            *lower_bound(temp.begin(), temp.end(), sequence[i]) = sequence[i];
        answer = max(answer, (int)(result[i] + temp.size() - 1));
    }

    cout << answer;

    return 0;
}
