using System.Drawing;

class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        {
            Console.SetIn(reader);

            int n = int.Parse(Console.ReadLine()!.Trim());
            int[] applies = Console.ReadLine()!.Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries).Select(int.Parse).ToArray();
            (int t, int p) = Console.ReadLine()!.Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries).Select(int.Parse).ToArray() switch { var arr => (arr[0], arr[1]) };

            int bundles = 0;
            foreach (int size in applies)
            {
                bundles += (size + t - 1) / t;
            }
            Console.WriteLine(bundles);
            Console.WriteLine($"{n / p} {n % p}");
        }
    }
}