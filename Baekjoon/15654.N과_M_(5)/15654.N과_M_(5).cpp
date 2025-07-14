#include <algorithm>
#include <iostream>
#include <deque>
#include <vector>

using namespace std;

void recursion(int N, int M, vector<bool> &isVisited, deque<int> &sequence, vector<int> &input)
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
        if (!isVisited[i])
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
    deque<int> sequence;
    vector<bool> isVisited(N);
    recursion(N, M, isVisited, sequence, input);
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;

    vector<int> input(N);
    for (int &term : input)
        cin >> term;

    sort(input.begin(), input.end());

    dfs(N, M, input);

    return 0;
}
