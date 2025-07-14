#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

void recursion(int N, int M, int start, vector<int> &sequence, vector<int> &input)
{
    if (sequence.size() == M)
    {
        for (int term : sequence)
            cout << term << ' ';
        cout << '\n';
        return;
    }

    for (int i = start; i < N; ++i)
    {
        if (!(i > start && input[i] == input[i - 1]))
        {
            sequence.push_back(input[i]);
            recursion(N, M, i, sequence, input);
            sequence.pop_back();
        }
    }
}

void dfs(int N, int M, vector<int> &input)
{
    vector<int> sequence;
    recursion(N, M, 0, sequence, input);
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;

    vector<int> input(N);
    for (int &number : input)
        cin >> number;
    sort(input.begin(), input.end());

    dfs(N, M, input);
    return 0;
}
