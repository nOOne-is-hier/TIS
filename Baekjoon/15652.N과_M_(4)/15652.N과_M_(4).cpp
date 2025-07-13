#include <iostream>
#include <deque>

using namespace std;

void recursive(int N, int M, int start, deque<int> &sequence)
{
    if (sequence.size() == M)
    {
        for (int num : sequence)
            cout << num << ' ';
        cout << '\n';
        return;
    }

    for (int i = start; i <= N; ++i)
    {
        sequence.push_back(i);
        recursive(N, M, i, sequence);
        sequence.pop_back();
    }
}

void dfs(int N, int M)
{
    deque<int> sequence;
    recursive(N, M, 1, sequence);
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;

    dfs(N, M);

    return 0;
}
