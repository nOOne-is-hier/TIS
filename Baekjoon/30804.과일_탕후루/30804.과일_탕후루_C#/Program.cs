class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        // using (var reader = new StreamReader(Console.OpenStandardInput()))
        {
            Console.SetIn(reader);

            int n = int.Parse(reader.ReadLine()!.Trim());
            int[] t = reader.ReadLine()!.Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries).Select(int.Parse).ToArray();
            int[] fruits = new int[10];
            int max = 0;

            int left = 0;

            for (int right = 0; right < n; right++)
            {
                fruits[t[right]]++;

                while (fruits.Count(x => x > 0) > 2)
                {
                    fruits[t[left]]--;
                    left++;
                }

                max = Math.Max(max, right - left + 1);
            }
            Console.Write(max);
        }
    }
}