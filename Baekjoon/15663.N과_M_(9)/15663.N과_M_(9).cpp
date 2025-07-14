#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

void recursion(int N, int M, vector<bool> &isVisited, vector<int> &sequence, vector<int> &input)
{
    if (sequence.size() == M)
    {
        for (int term : sequence)
            cout << term << ' ';
        cout << '\n';
        return;
    }

    for (int i = 0; i < N; ++i)
    {
        if (!(i > 0 && input[i - 1] == input[i] && !isVisited[i - 1]) && !isVisited[i])
        {
            isVisited[i] = true;
            sequence.push_back(input[i]);
            recursion(N, M, isVisited, sequence, input);
            isVisited[i] = false;
            sequence.pop_back();
        }
    }
}

void dfs(int N, int M, vector<int> &input)
{
    vector<bool> isVisited(N);
    vector<int> sequence;
    recursion(N, M, isVisited, sequence, input);
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
