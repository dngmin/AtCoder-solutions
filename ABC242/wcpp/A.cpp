#include <iostream>

int main()
{
    float A, B, C, X; std::cin >> A >> B >> C >> X;
    if (X <= A)
    {
        std::cout << 1;
    }
    else if (X > B)
    {
        std::cout << 0;
    }
    else
    {
        std::cout << C / (B - A);
    }
    return 0;
}