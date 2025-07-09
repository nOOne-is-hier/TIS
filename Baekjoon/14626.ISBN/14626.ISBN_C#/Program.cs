class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        {
            Console.SetIn(reader);

            string s = Console.ReadLine()!.Trim();
            int asterisk = s.IndexOf('*');
            int[] isbn = new int[13];

            for (int i = 0; i < 13; i++)
            {
                if (char.IsDigit(s[i])) isbn[i] = s[i] - '0';
            }

            for (int i = 0; i < 10; i++)
            {
                isbn[asterisk] = i;
                int temp = 0;
                for (int j = 0; j < 13; j++)
                {
                    if (j % 2 == 0)
                    {
                        temp += isbn[j];
                    }
                    else
                    {
                        temp += isbn[j] * 3;
                    }
                }
                if (temp % 10 == 0)
                {
                    Console.WriteLine(i);
                    break;
                }
            }
        }
    }
}