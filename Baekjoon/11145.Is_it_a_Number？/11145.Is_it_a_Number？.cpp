// Is it a Number? (11145)
// https://www.acmicpc.net/problem/11145

#include <iostream>
#include <regex>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    cin.ignore();

    regex pattern(R"(^\s*([0-9]+)\s*$)");

    while (T--)
    {
        string line;
        getline(cin, line);

        smatch m;
        if (!regex_match(line, m, pattern))
        {
            cout << "invalid input\n";
            continue;
        }

        string s = m[1].str();               // 숫자 부분만 (공백 제거된 상태)
        size_t p = s.find_first_not_of('0'); // 선행 0 스킵
        if (p == string::npos)
            cout << "0\n"; // 모두 0이면 "0"
        else
            cout << s.substr(p) << '\n'; // 선행 0 제거 출력
    }
}