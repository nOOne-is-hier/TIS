class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        // using (var reader = new StreamReader(Console.OpenStandardInput()))
        using (var writer = new StreamWriter(Console.OpenStandardOutput()))
        {
            int n = int.Parse(reader.ReadLine()!.Trim());
            PriorityQueue<int, int> pq = new PriorityQueue<int, int>();

            for (int i = 1; i <= n; i++)
            {
                int cal = int.Parse(reader.ReadLine()!.Trim());

                if (cal == 0) writer.WriteLine(pq.Count > 0 ? pq.Dequeue() : 0);
                else pq.Enqueue(cal, -cal);
            }
        }
    }
}