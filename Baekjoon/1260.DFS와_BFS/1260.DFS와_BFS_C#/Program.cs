class Program
{
    static void Dfs(int start, int nodes, PriorityQueue<int, int>[] adjacencyList)
    {
        bool[] isVisited = new bool[nodes];

        void DfsRecursive(int current)
        {
            while (adjacencyList[current].Count > 0)
            {
                int next = adjacencyList[current].Dequeue();
                if (!isVisited[next])
                {
                    isVisited[next] = true;
                    Console.Write($"{next + 1} ");
                    DfsRecursive(next);
                }
            }
        }

        isVisited[start] = true;
        Console.Write($"{start + 1} ");
        DfsRecursive(start);
    }

    static void Bfs(int start, int nodes, PriorityQueue<int, int>[] adjacencyList)
    {
        bool[] isVisited = new bool[nodes];
        LinkedList<int> deque = new LinkedList<int>(new[] { start });
        isVisited[start] = true;
        Console.Write($"{start + 1} ");

        while (deque.Any())
        {
            int current = deque.First!.Value;
            deque.RemoveFirst();

            while (adjacencyList[current].Count > 0)
            {
                int next = adjacencyList[current].Dequeue();
                if (!isVisited[next])
                {
                    isVisited[next] = true;
                    Console.Write($"{next + 1} ");
                    deque.AddLast(next);
                }
            }
        }
    }

    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        {
            Console.SetIn(reader);

            var (n, m, v) = Console.ReadLine()!.Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries).Select(int.Parse).ToArray() switch { var arr => (arr[0], arr[1], arr[2] - 1) };

            PriorityQueue<int, int>[] adjacencyListDfs = Enumerable.Range(0, n).Select(_ => new PriorityQueue<int, int>()).ToArray();
            PriorityQueue<int, int>[] adjacencyListBfs = Enumerable.Range(0, n).Select(_ => new PriorityQueue<int, int>()).ToArray();

            for (int i = 1; i <= m; i++)
            {
                var (s, e) = Console.ReadLine()!.Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries).Select(int.Parse).ToArray() switch { var arr => (arr[0] - 1, arr[1] - 1) };

                adjacencyListDfs[s].Enqueue(e, e);
                adjacencyListDfs[e].Enqueue(s, s);
                adjacencyListBfs[s].Enqueue(e, e);
                adjacencyListBfs[e].Enqueue(s, s);
            }

            Dfs(v, n, adjacencyListDfs);
            Console.WriteLine();
            Bfs(v, n, adjacencyListBfs);
        }
    }
}