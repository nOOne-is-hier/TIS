class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        {
            Console.SetIn(reader);

            string? s = Console.ReadLine();
            string[] ss = s!.Split(' ');
            double a = double.Parse(ss[0]);
            double b = double.Parse(ss[1]);
            Console.WriteLine(a / b);
        }

    }
}