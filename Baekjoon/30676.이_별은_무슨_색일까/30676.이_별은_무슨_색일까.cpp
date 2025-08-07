// 이 별은 무슨 색일까 (30676)
// https://www.acmicpc.net/problem/30676

#include <iostream>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int λ;

    cin >> λ;

    if (620 <= λ && λ <= 780)
        cout << "Red";
    else if (590 <= λ)
        cout << "Orange";
    else if (570 <= λ)
        cout << "Yellow";
    else if (495 <= λ)
        cout << "Green";
    else if (450 <= λ)
        cout << "Blue";
    else if (425 <= λ)
        cout << "Indigo";
    else if (380 <= λ)
        cout << "Violet";

    return 0;
}
