class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        {
            Console.SetIn(reader);
            int t = int.Parse(Console.ReadLine()!.Trim());
            int[] approaches = new int[11];

            for (int i = 1; i <= 10; i++)
            {
                for (int j = 1; j <= 3; j++)
                {
                    if (i - j >= 0)
                        approaches[i] += approaches[i - j] == 0 ? approaches[i - j] + 1 : approaches[i - j];
                    else break;
                }
            }

            for (int i = 1; i <= t; i++)
            {
                int n = int.Parse(Console.ReadLine()!.Trim());
                Console.WriteLine(approaches[n]);
            }
        }
    }
}