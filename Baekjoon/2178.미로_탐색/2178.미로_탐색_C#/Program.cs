class Program
{
    static (int r, int c)[] delta = new[] { (1, 0), (0, 1), (-1, 0), (0, -1) };

    static void Main()
    {
        using var reader = new StreamReader("input.txt");
        // using var reader = new StreamReader(Console.OpenStandardInput());
        using var writer = new StreamWriter(Console.OpenStandardOutput());

        // TODO: 풀이 로직 작성
        var (n, m) = reader.ReadLine()!
            .Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries)
            .Select(int.Parse).ToArray() switch
        { var arr => (arr[0], arr[1]) };

        string[] maze = new string[n];
        for (int i = 0; i < n; i++) maze[i] = reader.ReadLine()!.Trim();

        int[][] dist = Enumerable.Range(0, n).Select(_ => Enumerable.Repeat(int.MaxValue, m).ToArray()).ToArray();

        dist[0][0] = 1;
        Queue<(int cost, int r, int c)> q = new Queue<(int cost, int r, int c)>(new[] { (1, 0, 0) });

        while (q.Any())
        {
            var current = q.Dequeue();
            if (current.r == n - 1 && current.c == m - 1)
            {
                writer.WriteLine(current.cost);
                break;
            }

            for (int d = 0; d < 4; d++)
            {
                var (nr, nc) = (current.r + delta[d].r, current.c + delta[d].c);

                if (0 <= nr && nr < n && 0 <= nc && nc < m && maze[nr][nc] == '1' && dist[nr][nc] > current.cost + 1)
                {
                    dist[nr][nc] = current.cost + 1;
                    q.Enqueue((current.cost + 1, nr, nc));
                }
            }
        }
    }
}
