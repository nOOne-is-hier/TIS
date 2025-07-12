class Program
{
    static (int r, int c)[] delta = { (1, 0), (0, 1), (-1, 0), (0, -1) };
    static void Main()
    {
        using var reader = new StreamReader("input.txt");
        // using var reader = new StreamReader(Console.OpenStandardInput());
        using var writer = new StreamWriter(Console.OpenStandardOutput());

        int n = int.Parse(reader.ReadLine()!.Trim());

        string[] complex = Enumerable.Range(0, n).Select(_ => reader.ReadLine()!.Trim()).ToArray();

        bool[,] isVisited = new bool[n, n];

        var sizeOfComplexes = new PriorityQueue<int, int>();

        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
            {
                if (complex[i][j] == '1' && !isVisited[i, j])
                {
                    isVisited[i, j] = true;
                    int size = 0;
                    var q = new Queue<(int r, int c)>(new[] { (i, j) });

                    while (q.Any())
                    {
                        var current = q.Dequeue();
                        size++;
                        for (int d = 0; d < 4; d++)
                        {
                            var (nr, nc) = (current.r + delta[d].r, current.c + delta[d].c);

                            if (0 <= nr && nr < n && 0 <= nc && nc < n && !isVisited[nr, nc] && complex[nr][nc] == '1')
                            {
                                isVisited[nr, nc] = true;
                                q.Enqueue((nr, nc));
                            }
                        }
                    }
                    sizeOfComplexes.Enqueue(size, size);
                }
            }
        writer.WriteLine(sizeOfComplexes.Count);
        while (sizeOfComplexes.Count > 0) writer.WriteLine(sizeOfComplexes.Dequeue());
    }
}
