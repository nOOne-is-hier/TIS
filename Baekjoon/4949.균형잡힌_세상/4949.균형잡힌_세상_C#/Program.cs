class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        {
            Console.SetIn(reader);

            List<string> sentences = Console.In.ReadToEnd().Split('\n', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries).ToList();

            sentences.RemoveAt(sentences.Count - 1);

            foreach (string sentence in sentences)
            {
                Stack<char> stack = new Stack<char>();
                bool isValid = true;

                foreach (char c in sentence)
                {
                    if (c == '(' | c == '[')
                    {
                        stack.Push(c);
                    }
                    else if (c == ')' | c == ']')
                    {
                        if ((c == ')' && stack.Any() && stack.Peek() == '(') | (c == ']' && stack.Any() && stack.Peek() == '['))
                        {
                            stack.Pop();
                        }
                        else
                        {
                            isValid = false;
                            break;
                        }
                    }
                }
                Console.WriteLine(stack.Count == 0 && isValid ? "yes" : "no");
            }
        }
    }
}