#include <iostream>

int main()
{
    int X, Y; std::cin >> X >> Y;
    if (X >= Y) std::cout << 0;
    else std::cout << (Y - X) / 10 + ((Y - X)%10 == 0? 0 : 1);
    return 0;
}