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
            Stack<int> stack = new Stack<int>();
            Stack<char> result = new Stack<char>();
            int current = 1;

            for (int i = 1; i <= n; i++)
            {
                int term = int.Parse(reader.ReadLine()!.Trim());

                while (current <= term)
                {
                    stack.Push(current);
                    result.Push('+');
                    current++;
                }

                if (stack.Count > 0 && stack.Peek() == term)
                {
                    stack.Pop();
                    result.Push('-');
                }

                else
                {
                    writer.Write("NO");
                    return;
                }
            }
            writer.Write(string.Join('\n', result.Reverse()));
        }
    }
}