#include <iostream>

int main()
{
    std::cout.precision(10);
    double pi = 3.141592653589793, D;
    std::cin >> D;
    std::cout << pi * (D/2) * (D/2);
    return 0;
}