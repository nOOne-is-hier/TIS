class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        {
            Console.SetIn(reader);

            string[] s = Console.In.ReadToEnd().Split('\n', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries);
            int a = int.Parse(s[0]);
            int b = int.Parse(s[1]);
            int c = int.Parse(s[2]);
            Console.WriteLine(a + b - c);

            string concat = s[0] + s[1];
            Console.WriteLine(int.Parse(concat) - c);
        }
    }
}