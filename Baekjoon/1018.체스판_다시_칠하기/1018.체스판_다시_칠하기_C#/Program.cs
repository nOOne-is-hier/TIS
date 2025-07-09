class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        {
            Console.SetIn(reader);

            (int n, int m) = Console.ReadLine()!.Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries).Select(int.Parse).ToArray() switch { var arr => (arr[0], arr[1]) };
            bool[,] board = new bool[n, m];
            for (int r = 0; r < n; r++)
            {
                string s = Console.ReadLine()!.Trim();
                for (int c = 0; c < m; c++) board[r, c] = s[c] == 'W' ? true : false;
            }

            int min = int.MaxValue;
            for (int i = 0; i < n - 7; i++)
                for (int j = 0; j < m - 7; j++)
                {
                    bool isWhite = true;
                    for (int s = 0; s < 2; s++)
                    {
                        int temp = 0;
                        for (int r = i; r < i + 8; r++)
                            for (int c = j; c < j + 8; c++)
                            {
                                if ((r + c - i - j) % 2 == 0)
                                    if (board[r, c] != isWhite)
                                        temp++;

                                if ((r + c - i - j) % 2 == 1)
                                    if (board[r, c] == isWhite)
                                        temp++;
                            }
                        isWhite = !isWhite;
                        min = Math.Min(min, temp);
                    }
                }
            Console.WriteLine(min);
        }
    }
}