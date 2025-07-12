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

        var ladders = new Dictionary<int, int>();
        var snakes = new Dictionary<int, int>();

        for (int i = 1; i <= n + m; i++)
        {
            var (from, to) = reader.ReadLine()!
                .Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries)
                .Select(int.Parse).ToArray() switch
            { var arr => (arr[0] - 1, arr[1] - 1) };

            if (from < to) ladders.Add(from, to);
            else snakes.Add(from, to);
        }

        int[] board = Enumerable.Repeat(int.MaxValue, 100).ToArray();
        board[0] = 0;
        var q = new Queue<int>(new[] { 0 });

        while (q.Count > 0)
        {
            int current = q.Dequeue();

            for (int dice = 1; dice <= 6; dice++)
            {
                int next = current + dice;
                if (next >= 100) continue;

                if (ladders.TryGetValue(next, out var ladderDest)) next = ladderDest;
                else if (snakes.TryGetValue(next, out var snakeDest)) next = snakeDest;

                if (board[next] > board[current] + 1)
                {
                    board[next] = board[current] + 1;
                    q.Enqueue(next);
                }
            }
        }
        writer.Write(board[99]);
    }
}
