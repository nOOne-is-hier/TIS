class Program
{
    static int[] Dnq(int size, int[][] paper)
    {
        int[] papers = new int[2];

        void Recursion(int size, int r = 0, int c = 0)
        {
            int color = paper[r][c];
            bool isValid = true;

            for (int i = r; i < r + size; i++)
            {
                for (int j = c; j < c + size; j++)
                {
                    if (color != paper[i][j])
                    {
                        isValid = false;
                        break;
                    }
                }
                if (!isValid) break;
            }

            if (isValid) papers[color]++;

            else if (size > 1)
            {
                size /= 2;
                Recursion(size, r, c);
                Recursion(size, r, c + size);
                Recursion(size, r + size, c);
                Recursion(size, r + size, c + size);
            }
        }
        Recursion(size);
        return papers;
    }

    static void Main()
    {
        Console.SetIn(new StreamReader("input.txt"));

        int n = int.Parse(Console.ReadLine()!.Trim());

        int[][] paper = new int[n][];
        bool[,] isCompleted = new bool[n, n];
        int[] papers = new int[2];

        for (int i = 0; i < n; i++) paper[i] = Console.ReadLine()!.Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries).Select(int.Parse).ToArray();

        int[] result = Dnq(n, paper);

        Console.WriteLine(result[0]);
        Console.WriteLine(result[1]);

        // for (int p = (int)Math.Log2(n); p >= 0; p--)
        // {
        //     for (int sr = 0; sr < n; sr += (int)Math.Pow(2, (double)p))
        //         for (int sc = 0; sc < n; sc += (int)Math.Pow(2, (double)p))
        //         {
        //             if (!isCompleted[sr, sc])
        //             {
        //                 int area = 0;
        //                 int color = paper[sr][sc];
        //                 bool isVaild = true;
        //                 for (int cr = sr; cr < sr + (int)Math.Pow(2, (double)p); cr++)
        //                 {
        //                     for (int cc = sc; cc < sc + (int)Math.Pow(2, (double)p); cc++)
        //                     {
        //                         if (color == paper[cr][cc]) area++;
        //                         else
        //                         {
        //                             isVaild = false;
        //                             break;
        //                         }
        //                     }
        //                     if (!isVaild) break;
        //                 }

        //                 if (area == (int)Math.Pow(2, (double)p) * (int)Math.Pow(2, (double)p))
        //                 {
        //                     for (int cr = sr; cr < sr + (int)Math.Pow(2, (double)p); cr++)
        //                         for (int cc = sc; cc < sc + (int)Math.Pow(2, (double)p); cc++)
        //                             isCompleted[cr, cc] = true;
        //                     papers[paper[sr][sc]]++;
        //                 }
        //             }
        //         }
        // }
        // Console.WriteLine(papers[0]);
        // Console.WriteLine(papers[1]);
    }
}