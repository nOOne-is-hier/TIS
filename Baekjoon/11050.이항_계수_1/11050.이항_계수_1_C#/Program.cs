class Program
{
    static void Main()
    {
        static int fac(int a)
        {
            if (a <= 1) return 1;
            return a * fac(a - 1);
        }
        using (var reader = new StreamReader("input.txt"))
        {
            Console.SetIn(reader);
            int[] n = Console.ReadLine()!.Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries).Select(int.Parse).ToArray();
            int molecule = 1;
            for (int i = 1; i <= n[1]; i++)
            {
                molecule *= n[0];
                n[0]--;
            }
            Console.WriteLine(molecule / fac(n[1]));
        }
    }
}