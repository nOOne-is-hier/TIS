class Program
{
    static void Main()
    {
        using var reader = new StreamReader("input.txt");
        // using var reader = new StreamReader(Console.OpenStandardInput());
        using var writer = new StreamWriter(Console.OpenStandardOutput());

        // TODO: 풀이 로직 작성
        int n = int.Parse(reader.ReadLine()!.Trim());

        var pq = new PriorityQueue<int, (int, int)>();

        for (int i = 1; i <= n; i++)
        {
            int number = int.Parse(reader.ReadLine()!.Trim());

            if (number == 0)
                writer.WriteLine(pq.Count > 0 ? pq.Dequeue() : 0);

            else pq.Enqueue(number, number > 0 ? (number, number) : (-number, number));
        }
    }
}
