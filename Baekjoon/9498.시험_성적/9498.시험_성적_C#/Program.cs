class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        {
            Console.SetIn(reader);

            string s = Console.ReadLine()!;
            int n = int.Parse(s.Trim());

            Console.WriteLine((90 <= n && n <= 100) ? "A" : (80 <= n && n <= 89) ? "B" : (70 <= n && n <= 79) ? "C" : (60 <= n && n <= 69) ? "D" : "F");
        }
    }
}