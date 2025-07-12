class Program
{
    static char[] order = { 'D', 'S', 'L', 'R' };

    static void Main()
    {
        using var reader = new StreamReader("input.txt");
        // using var reader = new StreamReader(Console.OpenStandardInput());
        using var writer = new StreamWriter(Console.OpenStandardOutput());

        int t = int.Parse(reader.ReadLine()!.Trim());

        for (int i = 1; i <= t; i++)
        {
            var (from, to) = reader.ReadLine()!
                .Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries)
                .Select(int.Parse).ToArray() switch
            { var arr => (arr[0], arr[1]) };

            bool[] memo = new bool[10_000];
            memo[from] = true;
            var q = new Queue<(int, string)>(new[] { (from, "") });

            while (q.Count > 0)
            {
                var (current, orders) = q.Dequeue();

                if (current == to)
                {
                    writer.WriteLine(orders);
                    break;
                }

                foreach (char token in order)
                {
                    int next = token switch
                    {
                        'D' => current * 2 % 10000,
                        'S' => (current + 9999) % 10000,
                        'L' => (current % 1000) * 10 + current / 1000,
                        'R' => (current % 10) * 1000 + current / 10,
                        _ => throw new InvalidOperationException()
                    };

                    if (!memo[next])
                    {
                        memo[next] = true;
                        q.Enqueue((next, orders + token));
                    }
                }
            }
        }
    }
}
