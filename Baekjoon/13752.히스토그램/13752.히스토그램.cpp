#include <iostream>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;

    cin >> N;

    int K;

    while (N)
    {
        --N;
        cin >> K;

        while (K)
        {
            --K;
            cout << '=';
        }

        cout << '\n';
    }

    return 0;
}
