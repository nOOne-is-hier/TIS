using System.Runtime.InteropServices;

class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        {
            Console.SetIn(reader);

            (int a, int b, int v) = Console.ReadLine()!.Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries).Select(int.Parse).ToArray() switch { var arr => (arr[0], arr[1], arr[2]) };

            Console.WriteLine(Math.Ceiling((double)(v - a) / (a - b)) + 1);
        }
    }
}