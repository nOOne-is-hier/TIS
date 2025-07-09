class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        {
            Console.SetIn(reader);

            int n = int.Parse(Console.ReadLine()!.Trim());
            int[] timeByPeople = Console.ReadLine()!.Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries).Select(int.Parse).ToArray();

            Array.Sort(timeByPeople);

            for (int i = 1; i < n; i++) timeByPeople[i] += timeByPeople[i - 1];
            Console.WriteLine(timeByPeople.Sum());
        }
    }
}