using System.ComponentModel;

class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        using (var writer = new StreamWriter(Console.OpenStandardOutput()))
        {
            Console.SetIn(reader);

            int n = int.Parse(Console.ReadLine()!.Trim());
            int[] numbers = Console.ReadLine()!.Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries).Select(int.Parse).ToArray();
            HashSet<int> numberSet = new HashSet<int>(numbers);
            int m = int.Parse(Console.ReadLine()!.Trim());
            int[] numbersToFind = Console.ReadLine()!.Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries).Select(int.Parse).ToArray();
            foreach (int number in numbersToFind)
            {
                if (numberSet.Contains(number)) writer.WriteLine(1);
                else writer.WriteLine(0);
            }
        }
    }
}