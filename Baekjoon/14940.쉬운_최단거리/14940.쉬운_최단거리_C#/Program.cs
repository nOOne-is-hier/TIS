class Program
{
    static (int r, int c)[] delta = { (1, 0), (0, 1), (-1, 0), (0, -1) };
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

        int[][] map = Enumerable.Range(0, n).Select(_ => reader.ReadLine()!
            .Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries)
            .Select(int.Parse).ToArray()).ToArray();

        var start = Enumerable.Range(0, n).SelectMany(i => Enumerable.Range(0, m).Where(j => map[i][j] == 2).Select(j => (i, j))).FirstOrDefault();

        int[][] dist = Enumerable.Range(0, n)
        .Select(i => Enumerable.Range(0, m)
        .Select(j => map[i][j] == 0 ? 0 : int.MaxValue)
        .ToArray())
        .ToArray();

        var pq = new PriorityQueue<(int cost, int r, int c), int>(new[] { ((0, start.i, start.j), 0) });

        while (pq.Count > 0)
        {
            var current = pq.Dequeue();
            if (dist[current.r][current.c] <= current.cost) continue;
            dist[current.r][current.c] = current.cost;

            for (int d = 0; d < 4; d++)
            {
                var (nr, nc) = (current.r + delta[d].r, current.c + delta[d].c);
                if (0 <= nr && nr < n && 0 <= nc && nc < m && map[nr][nc] != 0 && dist[nr][nc] > current.cost + 1) pq.Enqueue((current.cost + 1, nr, nc), current.cost + 1);
            }
        }

        for (int i = 0; i < n; i++, writer.WriteLine())
            for (int j = 0; j < m; j++) writer.Write((dist[i][j] != int.MaxValue ? dist[i][j] : -1) + " ");
    }
}
