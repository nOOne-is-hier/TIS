#include <numeric>
#include <iostream>
#include <vector>

using namespace std;

int N, M;
int numberOfHouses;
int numberOfChickens;
vector<bool> isVisited;
vector<vector<int>> dist;
int result = 1e9;

void dfs(int last)
{
    if (accumulate(isVisited.begin(), isVisited.end(), 0) == M)
    {
        int temp = 0;
        for (int i = 0; i < numberOfHouses; ++i)
        {
            int candidate = 1e9;
            for (int j = 0; j < numberOfChickens; ++j)
                if (isVisited[j])
                    candidate = min(candidate, dist[i][j]);
            temp += candidate;
            if (result < temp)
                return;
        }
        result = min(result, temp);
    }

    for (int i = last; i < numberOfChickens; ++i)
    {
        isVisited[i] = true;
        dfs(i + 1);
        isVisited[i] = false;
    }
    return;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> M;

    vector<pair<int, int>> houses;
    vector<pair<int, int>> chickens;

    for (int r = 0; r < N; ++r)
        for (int c = 0; c < N; ++c)
        {
            int cell;
            cin >> cell;
            if (cell != 0)
                cell == 1 ? houses.push_back({r, c}) : chickens.push_back({r, c});
        }

    numberOfHouses = houses.size();
    numberOfChickens = chickens.size();

    dist.assign(numberOfHouses, vector<int>(numberOfChickens));

    for (int i = 0; i < numberOfHouses; ++i)
        for (int j = 0; j < numberOfChickens; ++j)
            dist[i][j] = abs(houses[i].first - chickens[j].first) + abs(houses[i].second - chickens[j].second);

    isVisited.assign(numberOfChickens, false);

    dfs(0);

    cout << result;

    return 0;
}
