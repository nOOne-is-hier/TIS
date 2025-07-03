class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        {
            Console.SetIn(reader);

            string s = Console.ReadLine()!;
            int[] ss = s.Split(' ').Select(int.Parse).ToArray();

            int sum = 0;
            foreach (int x in ss)
            {
                sum += x * x;
            }
            Console.WriteLine(sum % 10);
        }
    }
}