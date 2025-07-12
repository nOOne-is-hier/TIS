class Program
{
    static (int z, int r, int c)[] delta = { (1, 0, 0), (-1, 0, 0), (0, -1, 0), (0, 0, 1), (0, 1, 0), (0, 0, -1) };

    static void Main()
    {
        using var reader = new StreamReader("input.txt");
        // using var reader = new StreamReader(Console.OpenStandardInput());
        using var writer = new StreamWriter(Console.OpenStandardOutput());

        // TODO: 풀이 로직 작성
        var (m, n, h) = reader.ReadLine()!
            .Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries)
            .Select(int.Parse).ToArray() switch
        { var arr => (arr[0], arr[1], arr[2]) };

        int unriped = 0;
        int days = -1;
        var q = new Queue<(int z, int r, int c)>();

        int[][][] tomatoFarm = Enumerable.Range(0, h)
            .Select(z => Enumerable.Range(0, n)
            .Select(r =>
            {
                var row = reader.ReadLine()!
                            .Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries)
                            .Select((s, c) =>
                            {
                                int val = int.Parse(s);
                                if (val == 1) q.Enqueue((z, r, c));
                                else if (val == 0) unriped++;
                                return val;
                            }).ToArray();
                return row;
            }).ToArray()
            ).ToArray();

        while (q.Any())
        {
            var nq = new Queue<(int z, int r, int c)>();

            foreach (var (z, r, c) in q)
            {
                foreach (var (dz, dr, dc) in delta)
                {
                    var (nz, nr, nc) = (z + dz, r + dr, c + dc);

                    if (0 <= nz && nz < h && 0 <= nr && nr < n && 0 <= nc && nc < m && tomatoFarm[nz][nr][nc] == 0)
                    {
                        tomatoFarm[nz][nr][nc] = 1;
                        unriped--;
                        nq.Enqueue((nz, nr, nc));
                    }
                }
            }
            q = nq;
            days++;
        }
        writer.WriteLine(unriped == 0 ? days : -1);
    }
}
