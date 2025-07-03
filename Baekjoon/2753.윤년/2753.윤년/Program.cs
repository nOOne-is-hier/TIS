class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        {
            Console.SetIn(reader);

            string? s = Console.ReadLine();
            int n = int.Parse(s!.Trim());

            Console.WriteLine(((n % 4 == 0) && (n % 100 != 0) || (n % 400 == 0)) ? 1 : 0);
        }
    }
}