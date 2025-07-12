class Program
{
    static int[][][] tetrominoes = new int[][][]{
        new int [][]
        {
            new[] {1, 1, 1, 1}
        },
        new int [][]
        {
            new[] {1, 1},
            new[] {1, 1}

        },
        new int [][]
        {
            new[] {1, 0},
            new[] {1, 0},
            new[] {1, 1}
        },
        new int [][]
        {
            new[] {1, 0},
            new[] {1, 1},
            new[] {0, 1},
        },
        new int [][]
        {
            new[] {1, 1, 1},
            new[] {0, 1, 0}
        }
    };

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

        int[][] paper = Enumerable.Range(0, n)
            .Select(_ => reader.ReadLine()!
            .Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries)
            .Select(int.Parse)
            .ToArray())
            .ToArray();

        int max = 0;
        var variants = new List<int[][]>();
        foreach (var tetromino in tetrominoes)
        {
            int h = tetromino.Length;
            int w = tetromino[0].Length;
            var shape = tetromino;
            var rotated = new int[w][];
            for (int i = 0; i < w; i++) rotated[i] = new int[h];

            for (int d = 0; d < 4; d++)
            {
                for (int r = 0; r < h; r++)
                    for (int c = 0; c < w; c++) rotated[c][h - r - 1] = shape[r][c];

                variants.Add(rotated);
                h = rotated.Length;
                w = rotated[0].Length;
                shape = rotated;
                rotated = new int[w][];
                for (int i = 0; i < w; i++) rotated[i] = new int[h];
                var mirrored = new int[h][];
                for (int i = 0; i < h; i++) mirrored[i] = new int[w];

                for (int r = 0; r < h; r++)
                    for (int c = 0; c < w; c++) mirrored[r][w - c - 1] = shape[r][c];
                variants.Add(mirrored);
            }
        }

        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                foreach (var tetromino in variants)
                {
                    int h = tetromino.Length;
                    int w = tetromino[0].Length;
                    var (temp, size) = (0, 0);

                    for (int r = 0; r < h && r + i < n; r++)
                        for (int c = 0; c < w && c + j < m; c++)
                        {
                            if (tetromino[r][c] == 1)
                            {
                                temp += paper[r + i][c + j];
                                size++;
                            }
                        }
                    if (size == 4) max = Math.Max(max, temp);
                }
        writer.WriteLine(max);
    }
}