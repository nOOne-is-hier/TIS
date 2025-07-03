class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        {
            Console.SetIn(reader);

            int t = int.Parse(Console.ReadLine()!.Trim());

            for (int i = 1; i <= t; i++)
            {
                int[] input = Console.ReadLine()!.Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries).Select(int.Parse).ToArray();
                int h = input[0], w = input[1], n = input[2];
                int x = n % h;
                int y = n / h + 1;

                if (x == 0)
                {
                    x = h;
                    y -= 1;
                }

                string result = x.ToString() + y.ToString("D2");
                Console.WriteLine(result);
            }
        }
    }
}