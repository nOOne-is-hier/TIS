
class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        {
            Console.SetIn(reader);

            string? s = Console.ReadLine(); // "1 2"
            string[] ss = s!.Split(' ');
            int a = int.Parse(ss[0]);
            int b = int.Parse(ss[1]);
            Console.WriteLine(a + b);
        }
    }
}
