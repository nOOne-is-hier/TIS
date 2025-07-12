class Program
{
    static (int r, int c)[] delta = { (-1, 0), (0, 1), (1, 0), (0, -1) };

    static void Main()
    {
        using var reader = new StreamReader("input.txt");
        // using var reader = new StreamReader(Console.OpenStandardInput());
        using var writer = new StreamWriter(Console.OpenStandardOutput());

        // TODO: 풀이 로직 작성
        var (m, n) = reader.ReadLine()!
            .Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries)
            .Select(int.Parse).ToArray() switch
        { var arr => (arr[0], arr[1]) };

        int unriped = 0;
        int days = -1;
        var q = new Queue<(int r, int c)>();

        int[][] tomatoFarm = Enumerable.Range(0, n)
        .Select(r =>
            reader.ReadLine()!
                .Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries)
                .Select((s, c) =>
                {
                    int val = int.Parse(s);
                    if (val == 0) unriped++;
                    else if (val == 1) q.Enqueue((r, c));
                    return val;
                }
                ).ToArray())
        .ToArray();

        while (q.Any())
        {
            var nq = new Queue<(int r, int c)>();

            foreach (var (r, c) in q)
                foreach (var (dr, dc) in delta)
                {
                    var (nr, nc) = (r + dr, c + dc);

                    if (0 <= nr && nr < n && 0 <= nc && nc < m && tomatoFarm[nr][nc] == 0)
                    {
                        tomatoFarm[nr][nc] = 1;
                        unriped--;
                        nq.Enqueue((nr, nc));
                    }
                }
            q = nq;
            days++;
        }
        writer.Write(unriped == 0 ? days : -1);
    }
}
