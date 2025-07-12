class Program
{
    static void Main()
    {
        using var reader = new StreamReader("input.txt");
        // using var reader = new StreamReader(Console.OpenStandardInput());
        using var writer = new StreamWriter(Console.OpenStandardOutput());

        int t = int.Parse(reader.ReadLine()!.Trim());

        for (int i = 1; i <= t; i++)
        {
            int q = int.Parse(reader.ReadLine()!.Trim());

            var maxQ = new PriorityQueue<int, long>();
            var minQ = new PriorityQueue<int, int>();
            var memo = new Dictionary<int, int>();
            var size = 0;

            for (int j = 1; j <= q; j++)
            {
                (string cal, int number) = reader.ReadLine()!
                    .Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries)
                    .ToArray() switch
                { var arr => (arr[0], int.Parse(arr[1])) };

                if (cal == "I")
                {
                    maxQ.Enqueue(number, -(long)number);
                    minQ.Enqueue(number, number);
                    memo[number] = memo.GetValueOrDefault(number, 0) + 1;
                    size++;
                }

                else if (cal == "D" && number == 1 && size > 0)
                {
                    while (memo.GetValueOrDefault(maxQ.Peek(), 0) == 0) maxQ.Dequeue();
                    int max = maxQ.Dequeue();
                    memo[max]--;
                    size--;
                }

                else if (cal == "D" && number == -1 && size > 0)
                {
                    while (memo.GetValueOrDefault(minQ.Peek(), 0) == 0) minQ.Dequeue();
                    int min = minQ.Dequeue();
                    memo[min]--;
                    size--;
                }
            }
            if (size == 0) writer.WriteLine("EMPTY");
            else
            {
                while (memo.GetValueOrDefault(maxQ.Peek(), 0) == 0) maxQ.Dequeue();
                while (memo.GetValueOrDefault(minQ.Peek(), 0) == 0) minQ.Dequeue();
                writer.WriteLine($"{maxQ.Peek()} {minQ.Peek()}");
            }
        }
    }
}
