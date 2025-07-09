class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        {
            Console.SetIn(reader);

            int n = int.Parse(Console.ReadLine()!.Trim());

            (int weight, int height, int rank)[] peoples = new (int, int, int)[n];

            for (int i = 0; i < n; i++) peoples[i] = Console.ReadLine()!.Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries).Select(int.Parse).ToArray() switch { var arr => (arr[0], arr[1], 0) };

            for (int i = 0; i < n; i++)
            {
                int count = 0;
                for (int j = 0; j < n; j++)
                {
                    if (peoples[j].weight > peoples[i].weight && peoples[j].height > peoples[i].height) count++;
                }
                peoples[i] = (peoples[i].weight, peoples[i].height, ++count);
            }
            Console.WriteLine(string.Join(' ', peoples.Select(p => p.rank)));
        }
    }
}