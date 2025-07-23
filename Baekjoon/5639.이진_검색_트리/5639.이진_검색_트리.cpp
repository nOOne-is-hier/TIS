#include <iostream>
#include <vector>

using namespace std;

vector<int> preorder;

void postorder(int start, int end)
{
    if (start >= end)
        return;

    int root = preorder[start];
    int idx = start + 1;

    while (idx < end && preorder[idx] < root)
        ++idx;

    postorder(start + 1, idx);
    postorder(idx, end);
    cout << root << '\n';
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int node;
    while (cin >> node)
    {
        preorder.push_back(node);
    }

    postorder(0, preorder.size());

    return 0;
}
