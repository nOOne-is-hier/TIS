class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        {
            Console.SetIn(reader);

            int n = int.Parse(Console.ReadLine()!.Trim());
            (int age, int order, string name)[] members = new (int age, int order, string name)[n];
            for (int i = 0; i < n; i++) members[i] = Console.ReadLine()!.Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries).ToArray() switch { var arr => (int.Parse(arr[0]), i, arr[1]) };
            Array.Sort(members);
            foreach (var member in members) Console.WriteLine($"{member.age} {member.name}");
        }
    }
}