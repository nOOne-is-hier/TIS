#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

int solution(vector<string> friends, vector<string> gifts)
{
    int answer = 0;
    unordered_map<string, unordered_map<string, int>> table;
    unordered_map<string, pair<int, int>> gift_indices;

    for (string &gift : gifts)
    {
        char sp = gift.find(' ');
        string from = gift.substr(0, sp);
        string to = gift.substr(sp + 1);
        ++table[from][to];
        ++gift_indices[from].first;
        ++gift_indices[to].second;
    }

    for (string &to : friends)
    {
        int given = 0;
        for (string &from : friends)
            if (to != from)
            {
                if (table[to][from] && table[from][to] && table[to][from] > table[from][to])
                    ++given;
                else if (((table[to][from] && table[from][to] && table[to][from] == table[from][to]) || !table[from][to]) && gift_indices[to].first - gift_indices[to].second > gift_indices[from].first - gift_indices[from].second)
                    ++given;
            }
        answer = max(given, answer);
    }

    return answer;
}