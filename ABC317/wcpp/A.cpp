#include <iostream>

int main()
{
    int N, H, X, P;
    std::cin >> N >> H >> X;
    for (int i = 0; i < N; i++)
    {
        std::cin >> P;
        if (H+P >= X)
        {
            std::cout << i+1;
            return 0;
        }
    }
}