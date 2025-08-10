#include <algorithm>
#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> arr, int divisor)
{
    vector<int> answer;

    for (int num : arr)
        if (!(num % divisor))
            answer.push_back(num);

    sort(answer.begin(), answer.end());

    if (!answer.size())
        answer.push_back(-1);

    return answer;
}