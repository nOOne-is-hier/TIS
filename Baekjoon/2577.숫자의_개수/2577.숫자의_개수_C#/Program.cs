using System.Globalization;

class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        {
            Console.SetIn(reader);

            int a = int.Parse(Console.ReadLine()!.Trim());
            int b = int.Parse(Console.ReadLine()!.Trim());
            int c = int.Parse(Console.ReadLine()!.Trim());

            string result = (a * b * c).ToString();

            int[] dat = new int[10];

            foreach (char num in result)
            {
                dat[num - '0']++;
            }

            foreach (int cnt in dat)
            {
                Console.WriteLine(cnt);
            }
        }
    }
}