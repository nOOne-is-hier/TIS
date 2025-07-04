class Program
{
    static bool[] isPrime = Enumerable.Repeat(true, 1001).ToArray();

    static void Main()
    {
        isPrime[1] = false;
        for (int i = 2; i * i <= 1000; i++)
        {
            int multiplier = 2;
            while (multiplier * i <= 1000)
            {
                isPrime[multiplier * i] = false;
                multiplier++;
            }
        }
        using (var reader = new StreamReader("input.txt"))
        {
            Console.SetIn(reader);

            string _ = Console.ReadLine()!;
            int[] numbers = Console.ReadLine()!.Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries).Select(int.Parse).ToArray();

            int count = 0;
            foreach (int number in numbers)
            {
                if (isPrime[number])
                {
                    count += 1;
                }
            }
            Console.Write(count);
        }
    }
}