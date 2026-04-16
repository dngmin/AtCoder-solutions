#include <iostream>

int main()
{
    int N, A, total = 0;
    std::cin >> N;
    for (int i = 0; i < N*7; i++)
    {
        std::cin >> A;
        if (i > 0 & i%7 == 0)
        {
            std::cout << total << " ";
            total = 0;
        }
        total += A;
    }
    std::cout << total;
    return 0;
}