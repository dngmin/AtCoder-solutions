#include <iostream>

int main()
{
    int L1, R1, L2, R2, output = 0; std::cin >> L1 >> R1 >> L2 >> R2;
    int line[101] = {0};
    for (int i = L1; i < R1; i++)
    {
        line[i] += 1;
    }
    for (int i = L2; i < R2; i++)
    {
        line[i] += 1;
    }
    for (int l : line)
    {
        if (l == 2) output += 1;
    }
    std::cout << output;
    return 0;
}