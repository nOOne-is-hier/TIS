// 사과 (10833)
// https://www.acmicpc.net/problem/10833

#include <iostream>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;

    cin >> N;

    int rest = 0;
    int students = 0;
    int apple = 0;
    while (N--)
    {
        cin >> students >> apple;
        rest += apple % students;
    };

    cout << rest;

    return 0;
}
