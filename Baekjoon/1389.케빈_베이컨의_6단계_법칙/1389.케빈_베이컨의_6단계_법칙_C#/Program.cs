class Program
{
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

        int[][] adjacencyMatrix = new int[n][];
        for (int i = 0; i < n; i++) adjacencyMatrix[i] = Enumerable.Repeat(int.MaxValue, n).ToArray();

        for (int i = 1; i <= m; i++)
        {
            var (s, e) = reader.ReadLine()!
            .Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries)
            .Select(int.Parse).ToArray() switch
            { var arr => (arr[0] - 1, arr[1] - 1) };

            adjacencyMatrix[s][e] = adjacencyMatrix[e][s] = 1;
        }

        for (int c = 0; c < n; c++)
            for (int s = 0; s < n; s++)
                for (int e = 0; e < n; e++)
                    if (adjacencyMatrix[s][c] != int.MaxValue && adjacencyMatrix[c][e] != int.MaxValue && adjacencyMatrix[s][e] > adjacencyMatrix[s][c] + adjacencyMatrix[c][e])
                        adjacencyMatrix[s][e] = adjacencyMatrix[s][c] + adjacencyMatrix[c][e];

        PriorityQueue<int, (int, int)> pq = new PriorityQueue<int, (int, int)>();

        for (int i = 0; i < n; i++) pq.Enqueue(i + 1, (adjacencyMatrix[i].Sum(), i + 1));

        writer.WriteLine(pq.Dequeue());
    }
}
