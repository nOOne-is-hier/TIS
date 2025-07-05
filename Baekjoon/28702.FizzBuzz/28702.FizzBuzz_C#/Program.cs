using System.Reflection;

class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        {
            Console.SetIn(reader);

            string[] s = Console.In.ReadToEnd()!.Split('\n', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries).ToArray();

            for (int i = 0; i < 3; i++)
            {
                if (char.IsDigit(s[i][0]))
                {
                    int term = int.Parse(s[i]) + (3 - i);

                    if (term % 15 == 0) Console.WriteLine("FizzBuzz");
                    else if (term % 3 == 0) Console.WriteLine("Fizz");
                    else if (term % 5 == 0) Console.WriteLine("Buzz");
                    else Console.WriteLine(term);
                    break;
                }
            }


        }
    }
}