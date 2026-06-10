#include <iostream>

int main()
{
    int N, H, n, highest = 0;
    std::cin >> N;
    for (int i = 0; i < N; i++)
    {
        std::cin >> H;
        if (H > highest)
        {
            highest = H;
            n = i +1;
        }
    }
    std::cout << n;
    return 0;
}