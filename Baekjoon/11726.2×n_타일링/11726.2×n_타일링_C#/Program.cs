class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        {
            Console.SetIn(reader);

            int n = int.Parse(Console.ReadLine()!.Trim());

            int[] dp = new int[n];

            for (int i = 0; i < n; i++) dp[i] = (i - 2 >= 0 ? dp[i - 1] + dp[i - 2] : i + 1) % 10007;

            Console.WriteLine(dp[n - 1]);
        }
    }
}