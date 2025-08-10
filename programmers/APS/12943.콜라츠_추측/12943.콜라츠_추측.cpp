using namespace std;

int solution(int num)
{
    int answer = 0;

    while (answer < 500 && num != 1)
    {
        ++answer;

        if (num == 1)
            break;

        if (num % 2 == 0)
            num /= 2;
        else if (num % 2 == 1)
        {
            num *= 3;
            ++num;
        }
    }

    if (answer == 500 && num != 1)
        answer = -1;

    return answer;
}