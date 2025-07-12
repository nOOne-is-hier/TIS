class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        // using (var reader = new StreamReader(Console.OpenStandardInput()))
        using (var writer = new StreamWriter(Console.OpenStandardOutput()))
        {
            Console.SetIn(reader);

            int n = int.Parse(reader.ReadLine()!.Trim());

            PriorityQueue<int, int> pq = new PriorityQueue<int, int>();

            for (int i = 1; i <= n; i++)
            {
                int q = int.Parse(reader.ReadLine()!.Trim());

                if (q == 0)
                {
                    if (pq.Count > 0)
                        writer.WriteLine(pq.Dequeue());
                    else writer.WriteLine(0);
                }
                else pq.Enqueue(q, q);
            }
        }
    }
}