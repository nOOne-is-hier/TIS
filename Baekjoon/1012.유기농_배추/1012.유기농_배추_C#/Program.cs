class Program
{
    static (int r, int c)[] delta = { (1, 0), (0, 1), (-1, 0), (0, -1) };
    static void Main()
    {
        using (var reader = new StreamReader(("input.txt")))
        {
            Console.SetIn(reader);

            int t = int.Parse(Console.ReadLine()!.Trim());

            for (int i = 1; i <= t; i++)
            {
                var (m, n, k) = Console.ReadLine()!.Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries).Select(int.Parse).ToArray() switch { var arr => (arr[0], arr[1], arr[2]) };

                bool[,] field = new bool[n, m];

                for (int j = 1; j <= k; j++)
                {
                    var (c, r) = Console.ReadLine()!.Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries).Select(int.Parse).ToArray() switch { var arr => (arr[0], arr[1]) };

                    field[r, c] = true;
                }

                int worms = 0;

                for (int r = 0; r < n; r++)
                    for (int c = 0; c < m; c++)
                    {
                        if (field[r, c] == true)
                        {
                            LinkedList<(int, int)> deque = new LinkedList<(int, int)>(new[] { (r, c) });
                            field[r, c] = false;
                            worms++;

                            while (deque.Any())
                            {
                                var (cr, cc) = deque.First!.Value;
                                deque.RemoveFirst();

                                for (int d = 0; d < 4; d++)
                                {
                                    var (nr, nc) = (cr + delta[d].r, cc + delta[d].c);

                                    if (0 <= nr && nr < n && 0 <= nc && nc < m && field[nr, nc])
                                    {
                                        deque.AddLast((nr, nc));
                                        field[nr, nc] = false;
                                    }
                                }
                            }
                        }
                    }
                Console.WriteLine(worms);
            }
        }
    }
}