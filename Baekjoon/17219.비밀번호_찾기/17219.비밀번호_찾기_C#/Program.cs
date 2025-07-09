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

            Dictionary<string, string> pw = new Dictionary<string, string>();

            for (int i = 1; i <= n; i++)
            {
                string[] kv = reader.ReadLine()!.Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries);

                pw.Add(kv[0], kv[1]);
            }

            for (int i = 1; i <= m; i++) writer.WriteLine(pw[reader.ReadLine()!.Trim()]);
        }
    }
}