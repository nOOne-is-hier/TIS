using System.Formats.Asn1;
using System.Threading.Tasks.Dataflow;

class Program
{
    static bool[] primes = new bool[1_000_001];

    static void InitSieve()
    {
        if (primes[0]) return;
        primes[0] = primes[1] = true;
        for (int i = 2; i <= 1_000; i++)
        {
            int multiplier = 2;
            while (i * multiplier <= 1_000_000)
            {
                primes[i * multiplier] = true;
                multiplier++;
            }
        }
    }

    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        using (var writer = new StreamWriter(Console.OpenStandardOutput()))
        {
            Console.SetIn(reader);

            InitSieve();

            int[] number = Console.ReadLine()!.Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries).Select(int.Parse).ToArray();

            for (int i = number.Min(); i <= number.Max(); i++) if (!primes[i]) writer.WriteLine(i);
        }
    }
}