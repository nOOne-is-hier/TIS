class Program
{
    static void Main()
    {
        using var reader = new StreamReader("input.txt");
        // using var reader = new StreamReader(Console.OpenStandardInput());
        using var writer = new StreamWriter(Console.OpenStandardOutput());

        // TODO: 풀이 로직 작성
        int n = int.Parse(reader.ReadLine()!.Trim());

        int[][] graph = Enumerable.Range(0, n).Select(_ => reader.ReadLine()!
            .Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries)
            .Select(int.Parse).ToArray()).ToArray();

        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++) if (graph[i][j] == 0) graph[i][j] = int.MaxValue;

        for (int m = 0; m < n; m++)
            for (int s = 0; s < n; s++)
                for (int e = 0; e < n; e++)
                    if (graph[s][m] != int.MaxValue && graph[m][e] != int.MaxValue && graph[s][e] > graph[s][m] + graph[m][e]) graph[s][e] = graph[s][m] + graph[m][e];

        for (int i = 0; i < n; i++, writer.WriteLine())
            for (int j = 0; j < n; j++) writer.Write((graph[i][j] == int.MaxValue ? 0 : 1) + " ");
    }
}
