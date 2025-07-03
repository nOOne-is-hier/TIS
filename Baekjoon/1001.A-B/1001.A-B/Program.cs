class Program
{
    static void Main()
    {
        // using (var reader = new StreamReader("input.txt"))
        {
            Console.SetIn(new StreamReader("input.txt"));

            string? s = Console.ReadLine();
            string[] ss = s!.Split(' ');
            int a = int.Parse(ss[0]);
            int b = int.Parse(ss[1]);
            Console.WriteLine(a - b);
        }
    }
}