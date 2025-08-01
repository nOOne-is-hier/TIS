#include <iostream>
#include <vector>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, D;
    cin >> N >> D;
    vector<int> members(N);

    int problems = 0;
    for (int i = 0; i < N; ++i)
    {
        cin >> members[i];
        problems += members[i];
    }

    for (int i = 0; i < N; ++i)
        cout << members[i] * D / problems << '\n';

    return 0;
}
