class Program
{
    static void Main()
    {
        using (var reader = new StreamReader(Console.OpenStandardInput()))
        using (var writer = new StreamWriter(Console.OpenStandardOutput()))
        {
            // Console.SetIn(reader);

            int n = int.Parse(reader.ReadLine()!.Trim());
            int[] arr = new int[n];

            for (int i = 0; i < n; i++) arr[i] = int.Parse(reader.ReadLine()!.Trim());

            Array.Sort(arr);

            foreach (int num in arr) writer.WriteLine(num);
        }
    }
}