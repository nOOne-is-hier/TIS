class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        {
            Console.SetIn(reader);

            string? s = Console.ReadLine();
            int n = int.Parse(s!.Trim());

            for (int i = 1; i <= n; i++)
            {
                for (int j = 1; j <= i; j++)
                {
                    Console.Write('*');
                }
                Console.WriteLine();
            }
        }
    }
}