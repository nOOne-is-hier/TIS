class Program
{
    static long[] padovan = new long[100];
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        {
            Console.SetIn(reader);

            for (int i = 0; i < 100; i++)
            {
                padovan[i] = i - 3 >= 0 ? padovan[i - 2] + padovan[i - 3] : 1;
            }

            int t = int.Parse(Console.ReadLine()!.Trim());

            for (int i = 1; i <= t; i++)

                Console.WriteLine(padovan[int.Parse(Console.ReadLine()!.Trim()) - 1]);
        }
    }
}