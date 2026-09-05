#include <iostream>

int main()
{
    int X, Y; std::cin >> X >> Y;
    std::cout << ((X-Y)*(X-Y) < 9? "Yes" : "No");
    return 0;
}