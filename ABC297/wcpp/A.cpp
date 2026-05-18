#include <iostream>

int main()
{
    int N, D, T, T_prev;
    std::cin >> N >> D >> T_prev;
    for (int i = 1; i < N; i++)
    {
        std::cin >> T;
        if (T - T_prev <= D)
        {
            std::cout << T;
            return 0;
        }
        T_prev = T;
    }
    std::cout << -1;
    return 0;
}