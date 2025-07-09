using System.Numerics;

class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        {
            Console.SetIn(reader);

            int n = int.Parse(Console.ReadLine()!.Trim());
            BigInteger fac = 1;

            for (int i = n; i > 1; i--) fac *= i;

            string s = fac.ToString();

            for (int i = 0; i < s.Length; i++)
            {
                if (s[^(i + 1)] != '0')
                {
                    Console.WriteLine(i);
                    break;
                }
            }
        }
    }
}