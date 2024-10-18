#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <cstdio>
using namespace std;

bool isPerfectSquare(long long num) {
    long long root = static_cast<long long>(sqrt(num));
    return root * root == num;
}

int main() {
    int T;
    scanf("%d", &T);

    vector<long long> inputs(T);
    for (int i = 0; i < T; ++i) {
        scanf("%lld", &inputs[i]);
    }

    vector<string> results(T);
    for (int tc = 0; tc < T; ++tc) {
        long long N = inputs[tc];
        long long discriminant = 8 * N + 1;

        if (isPerfectSquare(discriminant)) {
            double value = sqrt(discriminant);
            results[tc] = "#" + to_string(tc + 1) + " " + to_string(static_cast<long long>((value - 1) / 2));
        } else {
            results[tc] = "#" + to_string(tc + 1) + " -1";
        }
    }

    for (const auto& result : results) {
        printf("%s\n", result.c_str());
    }

    return 0;
}