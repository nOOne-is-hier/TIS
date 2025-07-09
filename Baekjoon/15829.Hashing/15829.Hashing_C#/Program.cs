class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        {
            Console.SetIn(reader);

            int l = int.Parse(Console.ReadLine()!.Trim());
            string s = Console.ReadLine()!.Trim();

            long pow = 1;
            long hash = 0;

            foreach (char term in s)
            {
                int radix = term - 'a' + 1;
                hash = (hash + (radix * pow) % 1234567891) % 1234567891;
                pow = (pow * 31) % 1234567891;
            }

            Console.WriteLine(hash);
        }
    }
}