class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        using (var writer = new StreamWriter(Console.OpenStandardOutput()) { AutoFlush = false })
        {
            Console.SetIn(reader);

            int n = int.Parse(Console.ReadLine()!.Trim());
            int[] dat = new int[10001];
            for (int i = 1; i <= n; i++) dat[int.Parse(Console.ReadLine()!.Trim())]++;
            for (int i = 1; i <= 10000; i++)
            {
                for (int j = 1; j <= dat[i]; j++) writer.WriteLine(i);
            }

            writer.Flush();
        }
    }
}