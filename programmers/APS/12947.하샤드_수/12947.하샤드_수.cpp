using namespace std;

bool solution(int x)
{
    bool answer = true;
    int val_num = 0;
    int temp = x;

    while (temp)
    {
        val_num += temp % 10;
        temp /= 10;
    }

    answer = x % val_num ? false : true;

    return answer;
}