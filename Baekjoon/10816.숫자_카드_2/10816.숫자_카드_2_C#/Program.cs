class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        // using (var reader = new StreamReader(Console.OpenStandardInput()))
        using (var writer = new StreamWriter(Console.OpenStandardOutput()))
        {
            Console.SetIn(reader);

            int n = int.Parse(Console.ReadLine()!.Trim());
            Dictionary<int, int> cards = new Dictionary<int, int>();
            foreach (int card in Console.ReadLine()!.Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries).Select(int.Parse)) cards[card] = cards.GetValueOrDefault(card, 0) + 1;

            int m = int.Parse(Console.ReadLine()!.Trim());
            foreach (int card in Console.ReadLine()!.Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries).Select(int.Parse)) Console.Write(cards.GetValueOrDefault(card, 0) + " ");

        }
    }
}