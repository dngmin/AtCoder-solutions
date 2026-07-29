#include <iostream>

int main()
{
    float X; std::cin >> X;
    X *= 10;
    if ((int)X % 10 >= 5) X += 10;
    std::cout << (int)(X / 10);
    return 0;
}