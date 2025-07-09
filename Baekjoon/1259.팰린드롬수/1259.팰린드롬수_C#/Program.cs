class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        {
            Console.SetIn(reader);

            string[] numbers = Console.In.ReadToEnd()!.Split('\n', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries).ToArray();
            string[] result = new string[numbers.Length - 1];
            for (int i = 0; i < numbers.Length - 1; i++)
            {
                result[i] = numbers[i].SequenceEqual(numbers[i].Reverse()) ? "yes" : "no";
            }

            Console.Write(string.Join('\n', result));
        }
    }
}