class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        {
            Console.SetIn(reader);

            string s = Console.ReadLine()!;
            int n = int.Parse(s.Trim());

            string[] result = new string[n];
            for (int i = 1; i <= n; i++)
            {
                result[i - 1] = i.ToString();
            }
            Console.WriteLine(string.Join("\n", result));
        }
    }
}