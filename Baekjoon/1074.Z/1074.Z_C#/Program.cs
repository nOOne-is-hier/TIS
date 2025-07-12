class Program
{
    static void Main()
    {
        using var reader = new StreamReader("input.txt");
        // using var reader = new StreamReader(Console.OpenStandardInput());
        using var writer = new StreamWriter(Console.OpenStandardOutput());

        // TODO: 풀이 로직 작성
        var (n, r, c) = reader.ReadLine()!
            .Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries)
            .Select(int.Parse).ToArray() switch
        { var arr => (arr[0], arr[1], arr[2]) };

        int order = 0;

        for (int i = n - 1; i >= 0; i--)
        {
            int block = 0;

            if (r >= 1 << i)
            {
                r -= 1 << i;
                block += 2;
            }

            if (c >= 1 << i)
            {
                c -= 1 << i;
                block += 1;
            }

            order += block * (1 << i * 2);
        }
        writer.WriteLine(order);
    }
}
