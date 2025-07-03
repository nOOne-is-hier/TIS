class Program
{
    static void Main()
    {
        using (var reader = new StreamReader("input.txt"))
        {
            Console.SetIn(reader);

            string[] triangles = Console.In.ReadToEnd()!.Split('\n', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries);

            string[] result = new string[triangles.Length - 1];
            for (int i = 0; i < triangles.Length - 1; i++)
            {
                (int a, int b, int c) = triangles[i].Trim().Split(' ').Select(int.Parse).OrderBy(x => x).ToArray() switch { var arr => (arr[0], arr[1], arr[2]) };

                result[i] = (a * a + b * b == c * c) ? "right" : "wrong";
            }
            Console.Write(string.Join('\n', result));
        }
    }
}