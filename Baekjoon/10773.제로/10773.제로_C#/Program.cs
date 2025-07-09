using System.Collections.Immutable;

class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        {
            Console.SetIn(reader);

            int k = int.Parse(Console.ReadLine()!.Trim());
            Stack<int> stack = new Stack<int>();

            for (int i = 1; i <= k; i++)
            {
                int n = int.Parse(Console.ReadLine()!.Trim());
                if (n == 0) stack.Pop();
                else stack.Push(n);
            }
            Console.WriteLine(stack.Sum());
        }
    }
}