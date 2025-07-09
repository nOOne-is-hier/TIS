class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        {
            Console.SetIn(reader);

            int n = int.Parse(Console.ReadLine()!.Trim());
            int p = int.Parse(Console.ReadLine()!.Trim());
            LinkedList<int>[] adjacencyList = Enumerable.Range(0, n).Select(x => new LinkedList<int>()).ToArray();
            bool[] isInfested = new bool[n];

            for (int i = 0; i < p; i++)
            {
                var (a, b) = Console.ReadLine()!.Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries).Select(int.Parse).ToArray() switch { var arr => (arr[0], arr[1]) };
                adjacencyList[a - 1].AddLast(b - 1);
                adjacencyList[b - 1].AddLast(a - 1);
            }

            void Dfs(int start)
            {
                isInfested[start] = true;

                foreach (int next in adjacencyList[start])
                    if (!isInfested[next]) Dfs(next);
            }
            Dfs(0);
            Console.Write(isInfested.Count(x => x) - 1);
        }
    }
}