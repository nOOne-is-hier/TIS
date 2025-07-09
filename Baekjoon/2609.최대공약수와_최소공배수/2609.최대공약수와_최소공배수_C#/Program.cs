class Program
{
    static int gcd(int a, int b) => b == 0 ? a : gcd(b, (a % b));
    static void Main()
    {

        using (var reader = new StreamReader("input.txt"))
        {
            Console.SetIn(reader);

            int[] n = Console.ReadLine()!.Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries).Select(int.Parse).ToArray();

            int g = gcd(n.Max(), n.Min());
            int l = g * (n[0] / g) * (n[1] / g);

            Console.WriteLine($"{g}\n{l}");
        }
    }
}