class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        {
            Console.SetIn(reader);

            int n = int.Parse(Console.ReadLine()!.Trim());

            int[] dp = new int[n + 1];

            for (int i = 1; i <= n; i++)
            {
                dp[i] = int.MaxValue;
            }

            for (int r = 1; r <= n; r++)
            {
                int l = 1;

                while (r - l * l >= 0)
                {
                    dp[r] = Math.Min(dp[r], dp[r - l * l] + 1);
                    l++;
                }
            }

            Console.WriteLine(dp[n]);
        }
    }
}