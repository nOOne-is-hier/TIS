// Centroid of Point Masses (9945)
// https://www.acmicpc.net/problem/9945

#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long double N, x, y, m;
    int tc = 1;
    while (cin >> N)
    {
        long double sum_x = 0, sum_y = 0, sum_m = 0;

        if (N < 0)
            break;

        while (N > 0)
        {
            --N;
            cin >> x >> y >> m;
            sum_x += x * m;
            sum_y += y * m;
            sum_m += m;
        }

        cout << "Case " << tc << ": " << fixed << setprecision(2) << sum_x / sum_m << ' ' << sum_y / sum_m << '\n';
        ++tc;
    }

    return 0;
}
