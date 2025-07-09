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

            HashSet<string> unheard = new HashSet<string>();
            HashSet<string> unseen = new HashSet<string>();

            for (int i = 1; i <= n; i++) unheard.Add(reader.ReadLine()!.Trim());
            for (int i = 1; i <= m; i++) unseen.Add(reader.ReadLine()!.Trim());

            SortedSet<string> unheardAndUnseen = new SortedSet<string>(unheard.Intersect(unseen));

            writer.WriteLine(unheardAndUnseen.Count());
            foreach (string name in unheardAndUnseen) writer.WriteLine(name);
        }
    }
}