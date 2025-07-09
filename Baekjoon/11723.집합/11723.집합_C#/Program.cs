class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        // using (var reader = new StreamReader(Console.OpenStandardInput()))
        using (var writer = new StreamWriter(Console.OpenStandardOutput()))
        {
            Console.SetIn(reader);

            HashSet<int> set = new HashSet<int>();

            int n = int.Parse(reader.ReadLine()!.Trim());

            for (int i = 1; i <= n; i++)
            {
                (string order, int number) = reader.ReadLine()!.Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries).ToArray() switch { var arr => (arr[0], arr.Length > 1 ? int.Parse(arr[1]) : 0) };

                if (order == "add") set.Add(number);
                else if (order == "remove") set.Remove(number);
                else if (order == "check")
                    if (set.Contains(number)) writer.WriteLine(1);
                    else writer.WriteLine(0);
                else if (order == "toggle")
                    if (set.Contains(number)) set.Remove(number);
                    else set.Add(number);
                else if (order == "all") set = new HashSet<int>(Enumerable.Range(1, 20));
                else if (order == "empty") set.Clear();
            }
        }
    }
}