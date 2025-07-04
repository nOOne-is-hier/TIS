class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        {
            Console.SetIn(reader);

            (int n, int m) = Console.ReadLine()!.Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries).Select(int.Parse).ToArray() switch { var arr => (arr[0], arr[1]) };
            int[] numbers = Console.ReadLine()!.Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries).Select(int.Parse).ToArray();
            Array.Sort(numbers);

            int temp = 0;
            int result = 0;
            for (int i = 0; i < n - 2; i++)
            {
                temp += numbers[i];
                if (temp > m)
                {
                    temp -= numbers[i];
                    break;
                }

                for (int j = i + 1; j < n - 1; j++)
                {
                    temp += numbers[j];
                    if (temp > m)
                    {
                        temp -= numbers[j];
                        break;
                    }

                    for (int k = j + 1; k < n; k++)
                    {
                        temp += numbers[k];
                        if (temp > m)
                        {
                            temp -= numbers[k];
                            break;
                        }
                        if (temp > result) result = temp;
                        temp -= numbers[k];
                    }
                    temp -= numbers[j];
                }

                temp -= numbers[i];
            }
            Console.WriteLine(result);
        }
    }
}