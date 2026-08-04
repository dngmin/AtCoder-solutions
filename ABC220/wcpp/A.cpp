#include <iostream>

int main()
{
    int A, B, C; std::cin >> A >> B >> C;
    int mul = C;
    while (mul <= B)
    {
        if (A <= mul)
        {
            std::cout << mul;
            return 0;
        }
        mul += C;
    }
    std::cout << -1;
    return 0;
}