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
                int n = int.Parse(Console.ReadLine()!.Trim());

                Dictionary<string, int> closet = new Dictionary<string, int>();

                for (int j = 1; j <= n; j++)
                {
                    var (name, type) = Console.ReadLine()!.Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries).ToArray() switch { var arr => (arr[0], arr[1]) };

                    if (closet.ContainsKey(type)) closet[type] += 1;
                    else closet[type] = 1;

                }
                int result = 1;

                foreach (var kv in closet)
                {
                    result *= kv.Value + 1;
                }

                Console.WriteLine(result - 1);
            }
        }
    }
}