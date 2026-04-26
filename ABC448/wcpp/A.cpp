#include <iostream>

int main()
{
    int N, X, A;
    std::cin >> N >> X;
    for (int i = 0; i < N; i++)
    {
        std::cin >> A;
        if (A < X)
        {
            std::cout << 1 << std::endl;
            X = A;
        }
        else std::cout << 0 << std::endl;
    }
    return 0;
}