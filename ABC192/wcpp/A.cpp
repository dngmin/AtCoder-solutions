#include <iostream>

int main()
{
    int X; std::cin >> X;
    std::cout << (X % 100 == 0? 100 : 100 - (X % 100));
    return 0;
}