#include <iostream>

int main()
{
    int Y; std::cin >> Y;
    std::cout << (Y % 4 == 3? Y + 3 : Y + 2 - (Y % 4));
    return 0;
}