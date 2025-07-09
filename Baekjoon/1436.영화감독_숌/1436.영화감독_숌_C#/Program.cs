class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        {
            Console.SetIn(reader);

            int n = int.Parse(Console.ReadLine()!.Trim());

            int term = 0;
            string discriminator = "666";
            int start = 666;

            while (term < n)
            {
                if (start.ToString().Contains(discriminator))
                {
                    term++;
                    if (term == n)
                    {
                        Console.WriteLine(start);
                    }
                }
                start++;
            }
        }
    }
}