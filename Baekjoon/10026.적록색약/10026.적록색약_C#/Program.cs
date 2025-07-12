class Program
{
    static (int r, int c)[] delta = { (-1, 0), (0, 1), (1, 0), (0, -1) };

    static void Main()
    {
        using var reader = new StreamReader("input.txt");
        // using var reader = new StreamReader(Console.OpenStandardInput());
        using var writer = new StreamWriter(Console.OpenStandardOutput());

        int n = int.Parse(reader.ReadLine()!.Trim());

        char[,] normalPaint = new char[n, n];
        char[,] colorBlindPaint = new char[n, n];

        for (int i = 0; i < n; i++)
        {
            string line = reader.ReadLine()!.Trim();

            for (int j = 0; j < n; j++)
            {
                char color = line[j];
                normalPaint[i, j] = color;
                colorBlindPaint[i, j] = color == 'R' ? 'G' : color;
            }
        }

        for (int i = 0; i < 2; i++)
        {
            bool[,] isVisited = new bool[n, n];
            int zone = 0;

            for (int r = 0; r < n; r++)
                for (int c = 0; c < n; c++)
                {
                    if (!isVisited[r, c])
                    {
                        char color = i == 0 ? normalPaint[r, c] : colorBlindPaint[r, c];
                        isVisited[r, c] = true;
                        var q = new Queue<(int r, int c)>(new[] { (r, c) });

                        while (q.Any())
                        {
                            var (cr, cc) = q.Dequeue();

                            foreach (var (dr, dc) in delta)
                            {
                                var (nr, nc) = (cr + dr, cc + dc);
                                if (0 <= nr && nr < n && 0 <= nc && nc < n
                                    && !isVisited[nr, nc]
                                    && (i == 0 ? normalPaint[nr, nc] : colorBlindPaint[nr, nc]) == color)
                                {
                                    isVisited[nr, nc] = true;
                                    q.Enqueue((nr, nc));
                                }
                            }
                        }
                        zone++;
                    }
                }
            writer.Write(zone + " ");
        }
    }
}
