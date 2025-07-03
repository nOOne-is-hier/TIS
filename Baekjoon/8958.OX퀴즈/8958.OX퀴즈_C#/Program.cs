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
                string result = Console.ReadLine()!.Trim();

                int[] sheet = new int[80];

                for (int j = 1; j <= result.Length; j++)
                {
                    if (result[j - 1] == 'O')
                    {
                        sheet[j] = sheet[j - 1] + 1;
                    }
                }

                Console.WriteLine(sheet.Sum());
            }
        }
    }
}