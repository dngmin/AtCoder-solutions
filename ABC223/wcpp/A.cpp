#include <iostream>

int main()
{
    int X; std::cin >> X;
    std::cout << (X >= 100 and X%100 == 0? "Yes" : "No");
    return 0;
}