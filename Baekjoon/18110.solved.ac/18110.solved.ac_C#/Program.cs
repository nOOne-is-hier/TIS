class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        // using (var reader = new StreamReader(Console.OpenStandardInput()))
        {
            Console.SetIn(reader);

            int n = int.Parse(reader.ReadLine()!.Trim());

            if (n == 0)
            {
                Console.WriteLine(0);
                return;
            }

            int[] opinions = new int[31];

            for (int i = 1; i <= n; i++) opinions[int.Parse(reader.ReadLine()!.Trim())]++;

            int excluded = (int)Math.Round(n * 0.15, MidpointRounding.AwayFromZero);
            for (int i = 1; i <= excluded; i++)
            {
                for (int s = 1; s <= 30; s++)
                {
                    if (opinions[s] > 0)
                    {
                        opinions[s] -= 1;
                        break;
                    }
                }
                for (int e = 30; e >= 1; e--)
                {
                    if (opinions[e] > 0)
                    {
                        opinions[e] -= 1;
                        break;
                    }
                }
            }
            int sum = 0;
            for (int i = 1; i <= 30; i++) sum += opinions[i] * i;
            Console.WriteLine((int)Math.Round((double)sum / (n - excluded * 2), MidpointRounding.AwayFromZero));
        }
    }
}