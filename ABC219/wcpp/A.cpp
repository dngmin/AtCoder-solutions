#include <iostream>

int main()
{
    int X; std::cin >> X;
    if (X < 40) std::cout << 40 - X;
    else if (X < 70) std::cout << 70 - X;
    else if (X < 90) std::cout << 90 - X;
    else std::cout << "expert";
    return 0;
}