class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        {
            Console.SetIn(reader);

            int n = int.Parse(Console.ReadLine()!.Trim());

            for (int five = n / 5; five >= 0; five--)
            {
                int remaining = n - five * 5;
                if (remaining % 3 == 0)
                {
                    Console.WriteLine(five + remaining / 3);
                    return;
                }
            }
            Console.WriteLine(-1);
        }
    }
}