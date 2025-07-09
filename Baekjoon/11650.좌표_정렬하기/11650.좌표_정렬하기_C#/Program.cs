class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        {
            Console.SetIn(reader);

            int n = int.Parse(Console.ReadLine()!.Trim());
            (int x, int y)[] coordinates = new (int x, int y)[n];
            for (int i = 0; i < n; i++) coordinates[i] = Console.ReadLine()!.Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries).Select(int.Parse).ToArray() switch { var arr => (arr[0], arr[1]) };
            Array.Sort(coordinates);
            foreach (var coordinate in coordinates) Console.WriteLine($"{coordinate.x} {coordinate.y}");
        }
    }
}