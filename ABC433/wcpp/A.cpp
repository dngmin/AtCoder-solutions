#include <iostream>

int main()
{
    int X, Y, Z; std::cin >> X >> Y >> Z;
    std::cout << ((X-Z*Y)%(Z-1) == 0 && (X-Z*Y) >= 0? "Yes" : "No");
    return 0;
}