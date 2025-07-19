#include <iostream>
#include <set>
#include <vector>
// #include <queue>

using namespace std;

// 완전 탐색 풀이
// int N, M;
// int numOfBearers;
// vector<vector<int>> adjacencyList;
// vector<bool> knowsTruth;
// vector<vector<int>> parties;

int N, M, K;
vector<int> parent;
vector<int> truthKnowers;
vector<vector<int>> parties;
int result = 0;

int find(int x)
{
    return parent[x] == x ? x : find(parent[x]);
}

void unite(int a, int b)
{
    a = find(a);
    b = find(b);
    if (a != b)
        parent[b] = a;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> M >> K;

    parent.resize(N + 1);
    for (int i = 1; i <= N; ++i)
        parent[i] = i;
    truthKnowers.resize(K);
    parties.resize(M);

    for (int &truthKnower : truthKnowers)
        cin >> truthKnower;

    for (vector<int> &party : parties)
    {
        int participants = 0;
        cin >> participants;
        party.resize(participants);
        for (int &participant : party)
            cin >> participant;
    }

    for (int i = 0; i < M; ++i)
        for (int j = 1; j < parties[i].size(); ++j)
            unite(parties[i][0], parties[i][j]);

    set<int> s;
    for (int &truthKnower : truthKnowers)
        s.insert(find(truthKnower));

    for (vector<int> &party : parties)
    {
        bool canLie = true;
        for (int &participant : party)
        {
            if (s.count(find(participant)))
            {
                canLie = false;
                break;
            }
        }
        if (canLie)
            ++result;
    }

    cout << result;

    // 완전 탐색 풀이
    // cin >> N >> M >> numOfBearers;

    // knowsTruth.resize(N + 1);
    // parties.resize(M);
    // adjacencyList.resize(N + 1);

    // for (int i = 1; i <= numOfBearers; ++i)
    // {
    //     int x;
    //     cin >> x;
    //     knowsTruth[x] = true;
    // }

    // for (int i = 0; i < M; ++i)
    // {
    //     int participants;
    //     cin >> participants;

    //     for (int j = 0; j < participants; ++j)
    //     {
    //         int participant;
    //         cin >> participant;
    //         parties[i].push_back(participant);
    //     }

    //     for (int j = 0; j < participants; ++j)
    //         for (int k = j + 1; k < participants; ++k)
    //             if (j != k)
    //             {
    //                 adjacencyList[parties[i][j]].push_back(parties[i][k]);
    //                 adjacencyList[parties[i][k]].push_back(parties[i][j]);
    //             }
    // }

    // queue<int> q;
    // for (int i = 1; i <= N; ++i)
    //     if (knowsTruth[i])
    //         q.push(i);

    // while (!q.empty())
    // {
    //     int current = q.front();
    //     q.pop();

    //     for (int next : adjacencyList[current])
    //         if (!knowsTruth[next])
    //         {
    //             knowsTruth[next] = true;
    //             q.push(next);
    //         }
    // }

    // int result = 0;
    // for (int i = 0; i < M; ++i)
    // {
    //     bool isAbleToLie = true;
    //     for (int participant : parties[i])
    //         if (knowsTruth[participant])
    //         {
    //             isAbleToLie = false;
    //             break;
    //         }
    //     if (isAbleToLie)
    //         ++result;
    // }

    // cout << result;

    return 0;
}
