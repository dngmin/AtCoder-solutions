#include <iostream>

int main()
{
    int N; std::cin >> N;
    if (N / 1000 == 0)
    {
        std::cout << '0';
        if (N / 100 == 0)
        {
            std::cout << '0';
            if (N / 10 == 0)
            {
                std::cout << '0';
            }
        }
    }
    std::cout << N;
    return 0;
}