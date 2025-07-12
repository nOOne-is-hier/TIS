class Program
{
    static void Main()
    {
        using var reader = new StreamReader("input.txt");
        // using var reader = new StreamReader(Console.OpenStandardInput());
        using var writer = new StreamWriter(Console.OpenStandardOutput());

        // TODO: 풀이 로직 작성
        int n = int.Parse(reader.ReadLine()!.Trim());

        var pq = new PriorityQueue<(int, int), (int, int)>();

        for (int i = 1; i <= n; i++)
        {
            var (s, e) = reader.ReadLine()!
                .Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries)
                .Select(int.Parse).ToArray() switch
            { var arr => (arr[0], arr[1]) };

            pq.Enqueue((s, e), (e, s));
        }

        int last = -1;
        int sessions = 0;
        while (pq.Count > 0)
        {
            var (s, e) = pq.Dequeue();

            if (last <= s)
            {
                sessions++;
                last = e;
            }
        }
        writer.WriteLine(sessions);
    }
}
