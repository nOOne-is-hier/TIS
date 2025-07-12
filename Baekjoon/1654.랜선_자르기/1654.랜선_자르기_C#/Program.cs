class Program
{
    static void Main()
    {
        Console.SetIn(new StreamReader("input.txt"));

        var (k, n) = Console.ReadLine()!.Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries).Select(int.Parse).ToArray() switch { var arr => (arr[0], arr[1]) };

        int[] lines = new int[k];

        for (int i = 0; i < k; i++) lines[i] = int.Parse(Console.ReadLine()!.Trim());

        long l = 1;
        long r = lines.Max();
        long result = 0;

        while (l <= r)
        {
            long mid = (l + r) / 2;
            long temp = 0;

            foreach (int line in lines) temp += line / mid;

            if (temp >= n)
            {
                result = mid;
                l = mid + 1;
            }
            else r = mid - 1;
        }
        Console.WriteLine(result);
    }
}