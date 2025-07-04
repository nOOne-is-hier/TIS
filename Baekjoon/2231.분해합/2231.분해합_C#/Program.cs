class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        {
            Console.SetIn(reader);

            string s = Console.ReadLine()!.Trim();
            int length = s.Length;
            int n = int.Parse(s);
            int start = Math.Max(1, n - length * 9);

            for (int i = start; i <= n; i++)
            {
                if (i + i.ToString().Sum(c => c - '0') == n)
                {
                    Console.WriteLine(i);
                    return;
                }
            }
            Console.WriteLine(0);
        }
    }
}