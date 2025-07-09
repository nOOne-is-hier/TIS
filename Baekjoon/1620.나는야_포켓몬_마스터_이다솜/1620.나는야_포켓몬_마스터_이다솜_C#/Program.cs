using System.Xml;

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
            Dictionary<string, int> encyclopediaToString = new Dictionary<string, int>();
            Dictionary<int, string> encyclopediaToInteger = new Dictionary<int, string>();

            for (int i = 1; i <= n; i++)
            {
                string name = reader.ReadLine()!.Trim();
                encyclopediaToString.Add(name, i);
                encyclopediaToInteger.Add(i, name);
            }

            for (int i = 1; i <= m; i++)
            {
                string ask = reader.ReadLine()!.Trim();

                if (ask.All(char.IsDigit)) writer.WriteLine(encyclopediaToInteger[int.Parse(ask)]);
                else writer.WriteLine(encyclopediaToString[ask]);
            }
        }
    }
}