using System.Runtime.CompilerServices;

class Program
{
    static (int r, int c)[] delta = { (1, 0), (0, 1), (-1, 0), (0, -1) };

    static void Main()
    {
        using var reader = new StreamReader("input.txt");
        // using var reader = new StreamReader(Console.OpenStandardInput());
        using var writer = new StreamWriter(Console.OpenStandardOutput());

        // TODO: 풀이 로직 작성
        var (n, m) = reader.ReadLine()!
            .Split(' ', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries)
            .Select(int.Parse).ToArray() switch
        { var arr => (arr[0], arr[1]) };

        string[] campus = new string[n];

        for (int i = 0; i < n; i++) campus[i] = reader.ReadLine()!.Trim();

        (int r, int c) doYeon = (0, 0);

        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                if (campus[i][j] == 'I')
                {
                    doYeon = (i, j);
                    break;
                }

        bool[,] isVisited = new bool[n, m];
        isVisited[doYeon.r, doYeon.c] = true;
        var q = new Queue<(int, int)>(new[] { doYeon });
        int hasMet = 0;

        while (q.Any())
        {
            var (cr, cc) = q.Dequeue();

            for (int d = 0; d < 4; d++)
            {
                var (nr, nc) = (cr + delta[d].r, cc + delta[d].c);

                if (0 <= nr && nr < n && 0 <= nc && nc < m && "OP".Contains(campus[nr][nc]) && !isVisited[nr, nc])
                {
                    isVisited[nr, nc] = true;
                    q.Enqueue((nr, nc));
                    if (campus[nr][nc] == 'P') hasMet++;
                }
            }
        }

        writer.Write(hasMet > 0 ? hasMet : "TT");
    }
}
