class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        // using (var reader = new StreamReader(Console.OpenStandardInput()))
        {
            Console.SetIn(reader);

            int n = int.Parse(reader.ReadLine()!.Trim());
            int[] dat = new int[8_001];
            int sum = 0;
            int mid = n / 2 + 1;
            int current = 0;
            int median = 0;
            int mode = 0;
            int maxCount = 0;
            bool isSecond = true;
            bool isStart = false;
            int start = 0;
            int end = 0;

            for (int i = 1; i <= n; i++) dat[int.Parse(reader.ReadLine()!.Trim()) + 4000]++;

            for (int i = 0; i < 8_001; i++)
            {
                if (dat[i] > 0)
                {
                    sum += dat[i] * (i - 4000);

                    if (current < mid)
                    {
                        current += dat[i];
                        if (current >= mid) median = i - 4000;
                    }

                    if (maxCount < dat[i])
                    {
                        maxCount = dat[i];
                        mode = i - 4000;
                        isSecond = false;
                    }
                    else if (maxCount == dat[i] && !isSecond)
                    {
                        mode = i - 4000;
                        isSecond = true;
                    }

                    if (!isStart)
                    {
                        start = i - 4000;
                        isStart = true;
                    }
                    end = i - 4000;
                }
            }
            Console.Write($"{(int)Math.Round((double)sum / n, MidpointRounding.AwayFromZero)}\n{median}\n{mode}\n{end - start}");
        }
    }
}