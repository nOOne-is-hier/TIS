class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        // using (var reader = new StreamReader(Console.OpenStandardInput()))
        using (var writer = new StreamWriter(Console.OpenStandardOutput()))
        {
            // TODO: 풀이 로직 작성
            int n = int.Parse(reader.ReadLine()!.Trim());

            HashSet<int> set = new HashSet<int>();

            int[] input = reader.ReadLine()!.Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries).Select(int.Parse).ToArray();

            foreach (int term in input) set.Add(term);

            int[] arr = set.ToArray();

            Array.Sort(arr);

            Dictionary<int, int> dict = new Dictionary<int, int>();

            for (int i = 0; i < arr.Length; i++) dict.Add(arr[i], i);

            foreach (int term in input) writer.Write($"{dict[term]} ");
        }
    }
}
