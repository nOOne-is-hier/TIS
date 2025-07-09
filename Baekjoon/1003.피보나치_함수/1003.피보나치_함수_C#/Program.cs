class Program
{
    static int[,] memo = new int[41, 2];

    static (int zero, int one) Fibonacci(int n)
    {
        if (memo[n, 0] != 0 || memo[n, 1] != 0) return (memo[n, 0], memo[n, 1]);

        if (n == 0) return (memo[n, 0] = 1, memo[n, 1] = 0);
        if (n == 1) return (memo[n, 0] = 0, memo[n, 1] = 1);

        var (z1, o1) = Fibonacci(n - 2);
        var (z2, o2) = Fibonacci(n - 1);

        return (memo[n, 0] = z1 + z2, memo[n, 1] = o1 + o2);
    }

    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        using (var writer = new StreamWriter(Console.OpenStandardOutput()))
        {
            Console.SetIn(reader);

            int t = int.Parse(Console.ReadLine()!.Trim());

            for (int i = 1; i <= t; i++)
            {
                int n = int.Parse(Console.ReadLine()!.Trim());

                var (zero, one) = Fibonacci(n);
                writer.WriteLine($"{zero} {one}");
            }
        }
    }
}