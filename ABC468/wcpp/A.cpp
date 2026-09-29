#include <iostream>

int main()
{
    int N; std::cin >> N;
    int Ai, Ai1, Ai2; std::cin >> Ai >> Ai1;
    int output = 0;
    for (int i = 2; i < N; i++)
    {
        std::cin >> Ai2;
        output += (Ai < Ai1 and Ai1 > Ai2? 1 : 0);
        Ai = Ai1; Ai1 = Ai2;
    }
    std::cout << output;
    return 0;
}