class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        {
            Console.SetIn(reader);

            int t = int.Parse(Console.ReadLine()!.Trim());

            for (int i = 1; i <= t; i++)
            {
                int k = int.Parse(Console.ReadLine()!.Trim());
                int n = int.Parse(Console.ReadLine()!.Trim());
                int[,] apt = new int[k + 1, n];

                for (int r = 0; r <= k; r++)
                {
                    apt[r, 0] = 1;
                }

                for (int c = 0; c < n; c++)
                {
                    apt[0, c] = c + 1;
                }

                for (int r = 1; r <= k; r++)
                {
                    for (int c = 1; c < n; c++)
                    {
                        apt[r, c] = apt[r, c - 1] + apt[r - 1, c];
                    }
                }

                Console.WriteLine(apt[k, n - 1]);
            }

        }
    }
}