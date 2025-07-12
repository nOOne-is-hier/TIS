class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        // using (var reader = new StreamReader(Console.OpenStandardInput()))
        using (var writer = new StreamWriter(Console.OpenStandardOutput()))
        {
            // TODO: 풀이 로직 작성
            var (n, m, b) = reader.ReadLine()!.Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries).Select(int.Parse).ToArray() switch { var arr => (arr[0], arr[1], arr[2]) };

            int[] map = new int[n * m];

            for (int i = 0; i < n; i++)
            {
                int col = 0;
                foreach (int h in reader.ReadLine()!.Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries).Select(int.Parse))
                {
                    map[i * m + col] = h;
                    col++;
                }
            }

            PriorityQueue<(int time, int height), (int time, int height)> pq = new PriorityQueue<(int time, int height), (int time, int height)>();

            for (int h = 256; h >= 0; h--)
            {
                int time = 0;
                int block = b;

                foreach (int spot in map)
                {
                    if (spot > h)
                    {
                        time += (spot - h) * 2;
                        block += spot - h;
                    }
                    else if (spot < h)
                    {
                        time += h - spot;
                        block -= h - spot;
                    }
                }

                if (block >= 0) pq.Enqueue((time, h), (time, -h));
            }

            writer.WriteLine($"{pq.Peek().time} {pq.Peek().height}");
        }
    }
}
