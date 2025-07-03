class Program
{
    static void Main()
    {
        Func<int, int, string> compare = (x, y) => x > y ? ">" : (x < y ? "<" : "==");
        using (var reader = new StreamReader("input.txt"))
        {
            Console.SetIn(reader);

            string? s = Console.ReadLine();
            string[] ss = s!.Split(' ');
            int a = int.Parse(ss[0]);
            int b = int.Parse(ss[1]);

            Console.WriteLine(compare(a, b));
        }
    }
}