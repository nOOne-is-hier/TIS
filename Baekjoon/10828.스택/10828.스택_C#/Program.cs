class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        // using (var reader = new StreamReader(Console.OpenStandardInput()))
        using (var writer = new StreamWriter(Console.OpenStandardOutput()))
        {
            Console.SetIn(reader);

            int n = int.Parse(Console.ReadLine()!.Trim());
            Stack<int> stack = new Stack<int>();

            for (int i = 1; i <= n; i++)
            {
                (string order, int number) = Console.ReadLine()!.Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries).ToArray() switch { var arr => (arr[0], arr.Length > 1 ? int.Parse(arr[1]) : 0) };
                if (order == "push") stack.Push(number);
                else if (order == "pop")
                {
                    if (stack.Any()) writer.WriteLine(stack.Pop());
                    else writer.WriteLine(-1);
                }
                else if (order == "size") writer.WriteLine(stack.Count);
                else if (order == "empty")
                {
                    if (stack.Any()) writer.WriteLine(0);
                    else writer.WriteLine(1);
                }
                else if (order == "top")
                {
                    if (stack.Any()) writer.WriteLine(stack.Peek());
                    else writer.WriteLine(-1);
                }
            }
        }
    }
}