class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        {
            Console.SetIn(reader);

            int n = int.Parse(Console.ReadLine()!.Trim());

            int[] dp = new int[n + 1];

            for (int i = 2; i <= n; i++)
            {
                if (i % 6 == 0) dp[i] = new[] { dp[i / 3], dp[i / 2], dp[i - 1] }.Min() + 1;
                else if (i % 3 == 0) dp[i] = Math.Min(dp[i / 3], dp[i - 1]) + 1;
                else if (i % 2 == 0) dp[i] = Math.Min(dp[i / 2], dp[i - 1]) + 1;
                else dp[i] = dp[i - 1] + 1;
            }
            Console.Write(dp[n]);
        }
    }
}