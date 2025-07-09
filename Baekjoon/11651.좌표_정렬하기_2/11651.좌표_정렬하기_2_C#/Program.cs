using Microsoft.VisualBasic;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine()!.Trim());
        (int y, int x)[] coordinates = new (int y, int x)[n];
        for (int i = 0; i < n; i++) coordinates[i] = Console.ReadLine()!.Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries).Select(int.Parse).ToArray() switch { var arr => (arr[1], arr[0]) };
        Array.Sort(coordinates);
        foreach (var coordinate in coordinates) Console.WriteLine($"{coordinate.x} {coordinate.y}");
    }
}