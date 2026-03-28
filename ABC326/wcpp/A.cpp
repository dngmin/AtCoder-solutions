#include <iostream>

int main()
{
    int X, Y;
    std::cin >> X >> Y;
    std::cout << (-3 <= Y-X && Y-X <= 2? "Yes" : "No");
    return 0;
}