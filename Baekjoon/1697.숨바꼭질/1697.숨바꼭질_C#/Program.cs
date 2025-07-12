class Program
{
    static void Main()
    {
        using var reader = new StreamReader("input.txt");
        // using var reader = new StreamReader(Console.OpenStandardInput());
        using var writer = new StreamWriter(Console.OpenStandardOutput());

        // TODO: 풀이 로직 작성
        var (n, k) = reader.ReadLine()!
            .Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries)
            .Select(int.Parse).ToArray() switch
        { var arr => (arr[0], arr[1]) };

        int[] line = Enumerable.Repeat(int.MaxValue, 100_001).ToArray();

        line[n] = 0;
        Queue<int> q = new Queue<int>(new[] { n });

        while (q.Any())
        {
            int current = q.Dequeue();

            foreach (int next in new int[] { current - 1, current + 1, current * 2 })
            {
                if (0 <= next && next <= 100_000 && line[next] > line[current] + 1)
                {
                    line[next] = line[current] + 1;
                    q.Enqueue(next);
                }
            }
        }

        writer.WriteLine(line[k]);
    }
}
