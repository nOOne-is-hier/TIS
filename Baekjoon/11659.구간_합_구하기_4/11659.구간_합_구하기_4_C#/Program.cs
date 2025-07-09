class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        // using (var reader = new StreamReader(Console.OpenStandardInput()))
        using (var writer = new StreamWriter(Console.OpenStandardOutput()))
        {
            Console.SetIn(reader);

            (int n, int m) = reader.ReadLine()!.Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries).Select(int.Parse).ToArray() switch { var arr => (arr[0], arr[1]) };

            int[] numbers = reader.ReadLine()!.Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries).Select(int.Parse).ToArray();

            for (int i = 1; i < n; i++) numbers[i] += numbers[i - 1];

            for (int i = 1; i <= m; i++)
            {
                (int s, int e) = reader.ReadLine()!.Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries).Select(int.Parse).ToArray() switch { var arr => (arr[0], arr[1]) };
                writer.WriteLine(numbers[e - 1] - (s != 1 ? numbers[s - 2] : 0));
            }
        }
    }
}