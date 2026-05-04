#include <iostream>

int main()
{
    int X, Y;
    std::cin >> X >> Y;
    for (int i = 0; i < Y; i++) X *= 2;
    std::cout << X;
    return 0;
}