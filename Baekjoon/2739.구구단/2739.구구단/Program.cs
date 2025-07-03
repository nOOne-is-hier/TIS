class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        {
            Console.SetIn(reader);

            string? s = Console.ReadLine();
            int n = int.Parse(s!.Trim());

            for (int i = 1; i <= 9; i++)
            {
                Console.WriteLine($"{n} * {i} = {n * i}");
            }

        }
    }
}