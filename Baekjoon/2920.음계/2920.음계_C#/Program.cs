class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        {
            Console.SetIn(reader);

            int[] notes = Console.ReadLine()!.Split(' ').Select(int.Parse).ToArray();

            bool gradient;

            if (notes[0] < notes[1])
            {
                gradient = true;
            }
            else
            {
                gradient = false;
            }

            // for (int i = 1; i <= 6; i++)
            // {
            //     if ((notes[i] < notes[i + 1]) != gradient)
            //     {
            //         Console.WriteLine("mixed");
            //         Environment.Exit(0);
            //     }
            // }
            // Console.WriteLine(gradient ? "ascending" : "descending");

            bool isVaild = Enumerable.Range(1, 6).All(i => (notes[i] < notes[i + 1]) == gradient);

            if (!isVaild)
            {
                Console.WriteLine("mixed");
            }
            else
            {
                Console.WriteLine(gradient ? "ascending" : "descending");
            }
        }
    }
}