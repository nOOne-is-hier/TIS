class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        {
            Console.SetIn(reader);

            (int n, int k) = Console.ReadLine()!.Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries).Select(int.Parse).ToArray() switch { var arr => (arr[0], arr[1]) };
            Stack<int> coins = new Stack<int>();

            for (int i = 1; i <= n; i++) coins.Push(int.Parse(Console.ReadLine()!.Trim()));
            int changes = 0;

            while (coins.Any())
            {
                int amount = coins.Pop();
                if (amount <= k) changes += k / amount;
                k %= amount;
            }
            Console.Write(changes);
        }
    }
}