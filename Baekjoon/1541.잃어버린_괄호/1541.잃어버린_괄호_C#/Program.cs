using System.Text.RegularExpressions;

class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        {
            Console.SetIn(reader);

            string expression = Console.ReadLine()!.Trim();
            int total = 0;
            bool minusMode = false;
            string[] tokens = Regex.Split(expression, @"([+-])");

            foreach (string token in tokens)
            {
                if (token == "-") minusMode = true;
                else if (token == "+") continue;
                else
                {
                    total += minusMode ? -int.Parse(token) : int.Parse(token);
                }
            }

            Console.WriteLine(total);
        }
    }
}