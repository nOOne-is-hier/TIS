class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        // using (var reader = new StreamReader(Console.OpenStandardInput()))
        {
            var (n, m) = reader.ReadLine()!.Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries).Select(int.Parse).ToArray() switch { var arr => (arr[0], arr[1]) };

            List<int>[] adjacencyList = new List<int>[n];
            for (int i = 0; i < n; i++) adjacencyList[i] = new List<int>();

            for (int i = 1; i <= m; i++)
            {
                var (s, e) = reader.ReadLine()!.Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries).Select(int.Parse).ToArray() switch { var arr => (arr[0] - 1, arr[1] - 1) };
                adjacencyList[s].Add(e);
                adjacencyList[e].Add(s);
            }

            int trees = 0;
            bool[] isVisited = new bool[n];

            for (int i = 0; i < n; i++)
            {
                if (!isVisited[i])
                {
                    Queue<int> q = new Queue<int>(new int[] { i });
                    isVisited[i] = true;
                    trees++;

                    while (q.Any())
                    {
                        int current = q.Dequeue();
                        foreach (int next in adjacencyList[current])
                        {
                            if (!isVisited[next])
                            {
                                isVisited[next] = true;
                                q.Enqueue(next);
                            }
                        }
                    }
                }
            }
            Console.WriteLine(trees);
        }
    }
}