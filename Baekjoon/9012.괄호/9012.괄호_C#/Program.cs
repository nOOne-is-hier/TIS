class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        {
            Console.SetIn(reader);

            int t = int.Parse(Console.ReadLine()!.Trim());

            for (int i = 1; i <= t; i++)
            {
                string s = string.Join("", Console.ReadLine()!.Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries));

                Stack<char> stack = new Stack<char>();
                bool isValid = true;

                foreach (char c in s)
                {
                    if (c == '(')
                    {
                        stack.Push(c);
                    }
                    else if (c == ')')
                    {
                        if (!stack.Any())
                        {
                            isValid = false;
                            break;
                        }
                        stack.Pop();
                    }
                }
                if (stack.Count == 0 && isValid) Console.WriteLine("YES");
                else Console.WriteLine("NO");
            }
        }
    }
}