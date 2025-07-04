class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        {
            Console.SetIn(reader);

            long n = long.Parse(Console.ReadLine()!.Trim());

            double approx = ((Math.Sqrt(12 * n - 3) + 3) / 6);
            Console.WriteLine(Math.Ceiling(approx));
        }
    }
}