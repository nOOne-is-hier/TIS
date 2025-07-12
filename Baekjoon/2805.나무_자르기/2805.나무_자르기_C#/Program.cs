class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        // using (var reader = new StreamReader(Console.OpenStandardInput()))
        {
            Console.SetIn(reader);

            var (n, m) = reader.ReadLine()!.Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries).Select(int.Parse).ToArray() switch { var arr => (arr[0], arr[1]) };
            int[] trees = reader.ReadLine()!.Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries).Select(int.Parse).ToArray();

            long l = 0;
            long r = trees.Max();
            long result = 0;

            while (l <= r)
            {
                long mid = (l + r) / 2;
                long temp = 0;

                foreach (int tree in trees) if (tree > mid) temp += tree - mid;

                if (temp >= m)
                {
                    l = mid + 1;
                    result = mid;
                }
                else r = mid - 1;
            }
            Console.WriteLine(result);
        }
    }
}