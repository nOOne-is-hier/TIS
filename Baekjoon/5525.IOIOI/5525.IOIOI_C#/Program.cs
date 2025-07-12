class Program
{
    static void Main()
    {
        using var reader = new StreamReader("input.txt");
        // using var reader = new StreamReader(Console.OpenStandardInput());
        using var writer = new StreamWriter(Console.OpenStandardOutput());

        // TODO: 풀이 로직 작성
        int n = int.Parse(reader.ReadLine()!.Trim());
        int s = int.Parse(reader.ReadLine()!.Trim());
        string line = reader.ReadLine()!.Trim();

        int result = 0;
        int count = 0;
        int i = 1;

        while (i < s - 1)
        {
            if (line[i - 1] == 'I' && line[i] == 'O' && line[i + 1] == 'I')
            {
                count++;
                if (count == n)
                {
                    result++;
                    count--;
                }
                i += 2;
            }
            else
            {
                count = 0;
                i++;
            }
        }
        writer.WriteLine(result);
    }
}
